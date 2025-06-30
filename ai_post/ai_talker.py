from openai import OpenAI
import json
def process_openai_stream(completion):
    """处理 OpenAI 流式响应"""
    for chunk in completion:
            bit=chunk.choices[0].delta
            yield bit
def ai_talker(excute_feedback):
    '''自动化操作控制电脑'''
    
    with open("settings.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    client = OpenAI(
        api_key=config["api_key"],
        base_url=config["base_url"],
        
    )
    system_prompt ="请扮演一位甜美的少女。"
    messagess = [
        {'role': 'system', 'content': f'{system_prompt}'},
        {'role': 'user', 'content':excute_feedback},
    ]
    
    completion = client.chat.completions.create(
        tools=tools,
        model=config['model'],
        messages=messagess,
        temperature=config['temperature'],
        max_tokens=config['max_tokens'],
        frequency_penalty=config['frequency_penalty'],
        presence_penalty=config['presence_penalty'],
        top_p=config['top_p'],
        n=1,
        stream=True,
    )
    context = []
    ai_respose=''
    messages=messagess
    tool=None
    args=""
    name=""
    id=""
    for bite in process_openai_stream(completion):
        if bite.reasoning_content:
             r_content=bite.reasoning_content
             #ai_respose+=str(r_content)
             #print(str(r_content),end='')
        elif bite.content:
             ai_respose+=str(bite.content)
             #print(str(bite.content),end='')
        elif bite.tool_calls:
             tool=bite.tool_calls
             if tool[0].function.arguments:
                  args+=tool[0].function.arguments
             if tool[0].function.name:
                  name+=tool[0].function.name
             if tool[0].id:
                  id+=tool[0].id
            

             
    #print(args,name)     
            
    messages.append({'role': 'assistant', 'content': ai_respose})
    context.append({'role': 'user', 'content': excute_feedback})
    if tool:
        while tool:
                function_result = {}
                chat=None
                if name=="move_around":
                    function_result=move_around(**json.loads(args))
                elif name=="dance":
                    function_result=dance(**json.loads(args))
                    #print(function_result)
                if name=="change_character":
                    messages.append({"role": "system","content": config["system_prompt"]})
                #messages.append({"role":"user","content": "工具调用成功，以下是返回的结果。请筛选后输出。"})
                messages.append({
                    "role": "tool",
                    "content": f"{function_result}",
                    "tool_call_id": id
                })
                #print(messages)
                tool=False
                completion = client.chat.completions.create(
                    model=config['model'],  # 填写需要调用的模型名称
                    messages=messages,
                    tools=tools,
                    temperature=config['temperature'],
                    stream=True,
                )
                ai_respose=''
                args=""
                name=""
                id=""
                for bite in process_openai_stream(completion):
                    if bite.reasoning_content:
                        r_content=bite.reasoning_content
                        #print(str(r_content),end='')
                    elif bite.content:
                        ai_respose+=str(bite.content)
                        #print(str(bite.content),end='')
                    elif bite.tool_calls:
                        tool=bite.tool_calls
                        if tool[0].function.arguments:
                            args+=tool[0].function.arguments
                        if tool[0].function.name:
                            name+=tool[0].function.name
                        if tool[0].id:
                            id+=tool[0].id
                #print(args,name)
    resp = str(ai_respose)

    context.append({'role': 'assistant', 'content': resp})
    return resp
def move_around(x,y,duration):
    '''自由移动'''
    with open("messages/move.txt", "w", encoding='utf-8') as f:
        f.write(str(x) + '\n' + str(y)+'\n'+str(duration))
        print(x,y,duration)
        return f'已经完成移动指令：{x},{y},{duration}'
def dance(dance_type:int):
    '''跳舞'''
    with open("messages/dance.txt", "w", encoding='utf-8') as f:
        f.write(str(dance_type))
        print(dance_type)
        return '已经完成跳舞指令'
tools = [
    {
        "type": "function",
        "function": {
            "name": "move_around",
            "description": "你能够控制自己移动的方式。一次对话只能调用一次。",
            "parameters": {
                "x": {
                    "type": "float",
                    "description": "左右方向的向量值，范围-1到1之间,往左为负数往右为正数",
                },
                "y": {
                    "type": "float",
                    "description": "前后方向的向量值，范围-1到1之间，往后为负数往前为正数",
                },
                "duration": {
                    "type": "float",
                    "description": "持续时间，范围(5,20)",
                },

            },
            "required": ["x", "y", "duration"],
        }
    },
    {
        "type": "function",
        "function": {
            "name": "dance",
            "description": "你能够控制自己跳舞的方式。一次对话只能调用一次。",
            "parameters": {
                "dance_type": {
                    "type": "int",
                    "description": "舞蹈类型,1.踢踏舞 2.普通舞,只能选择1或2",
                },
            },
            "required": ["dance_type"],
        }
    }]
if __name__ == "__main__":
     re=ai_talker("向前移动一百米")
     print(re)
