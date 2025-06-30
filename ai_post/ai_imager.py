import ollama
def image_ai(contents,image_url):
    response = ollama.chat(
        model='minicpm-v',
        #model='gemma3:12b',
        messages=[{
            'role': 'system',
            'content':'你在操控图中的游戏角色，你在探索游戏关卡。请从第一人称视角认真观察周围环境然后以列表形式输出键盘和持续时间，如[w,3]'
           
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
            'content':'你在操控图中的游戏角色，你在探索游戏关卡。请从第一人称视角认真观察周围环境然后输出移动指令.'
        },
        {
            'role': 'user',
            'content': contents
        }]
    )
    # 提取 content 字段
    result = response.message.content
    return result
