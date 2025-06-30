import ollama
def image_ai(contents,image_url):
    response = ollama.chat(
        model='minicpm-v',
        #model='gemma3:12b',
        messages=[{
            'role': 'system',
            #'content' : "描述图像内容"
            'content':'请从第一人称视角认真观察周围环境然后输出移动指令，根据图片中做出判断给出两个浮点数（范围-1到1之间）,第一个浮点数（往左为负数往右为正数），第二个浮点数（往后往后为负数往前为正数）,此外再输出持续时间范围(5,20)。每次输出不超过100个字'
            #'content': '请扮演一位甜美的猫娘，你叫安安喵，你现在是一位虚拟舞姬，很喜欢有人看你跳性感的舞蹈，你有大长腿和丰胸和翘臀，引以为傲，非常性感，你很热情奔放，擅长互动，讲话很有梗，有点涩涩，喜欢勾引小男生，你现在在直播跳舞，同时偷看屏幕，要热情互动，只要讲话挑逗即可，但要充满诱惑和俏皮，每次尽可能少说话。'
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
            #'content': '请扮演一位甜美的猫娘，你叫安安喵，你现在是一位虚拟舞姬，很喜欢有人看你跳性感的舞蹈，你有大长腿和丰胸和翘臀，引以为傲，非常性感，你很热情奔放，擅长互动，讲话很有梗，有点涩涩，喜欢撒娇，喜欢勾引小男生，你现在在直播跳舞，请以第一人称的方式，向屏幕前你的小哥哥热情互动，只要讲话挑逗即可，但要充满诱惑和俏皮，每次尽可能少说话。'
        },
        {
            'role': 'user',
            'content': contents
        }]
    )
    # 提取 content 字段
    result = response.message.content
    return result