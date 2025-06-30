import ollama
def image_ai(contents,image_url):
    response = ollama.chat(
        model='minicpm-v',
        #model='gemma3:12b',
        messages=[{
            'role': 'system',
            #'content' : "描述图像内容"
            'content':'请从第一人称视角认真观察周围环境然后输出移动指令，根据图片中做出判断给出两个浮点数（范围-1到1之间）,第一个浮点数（往左为负数往右为正数），第二个浮点数（往后往后为负数往前为正数）,此外再输出持续时间范围(5,20)。每次输出不超过100个字'
            
        },
        {
            'role': 'user',
            'content': contents,
            'images': [image_url]
        }]
    )
    # 提取 content 字段
    result = response.message.content
    return result
def talk_ai(contents):
    response = ollama.chat(
        model='gemma2',
        messages=[{
            'role': 'system',
            'content':'你在操控图中的游戏角色，你在探索游戏关卡。请从第一人称视角认真观察周围环境然后输出移动指令，根据图片中做出判断给出两个浮点数（范围-1到1之间）,第一个浮点数（往左为负数往右为正数），第二个浮点数（往后往后为负数往前为正数）。'
        },
        {
            'role': 'user',
            'content': contents
        }]
    )
    # 提取 content 字段
    result = response.message.content
    return result
