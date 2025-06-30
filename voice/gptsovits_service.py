import os
import requests

# 获取当前脚本的绝对路径
script_path = os.path.abspath(__file__)

# print("当前脚本的绝对路径是:", script_path)

audio_output_dir = script_path.replace(os.path.basename(script_path), "audio_output")
print("音频输出目录是:", audio_output_dir)

service_location = "http://127.0.0.1:9880"
ya_refer_wav_path="D:/AI/GPT-SoVITS-v3lora-20250228/refer_audio/雅/难过_sad/【难过_sad】很遗憾，除了能从DNA发现死者是男性外，我们比对了全市有记录的失踪者与犯罪者的DNA没有发现匹配记录。.wav"
ya_prompt_text="很遗憾，除了能从DNA发现死者是男性外，我们比对了全市有记录的失踪者与犯罪者的DNA没有发现匹配记录。"
laikaen_refer_wav_path="D:/AI/GPT-SoVITS-v3lora-20250228/refer_audio/莱卡恩/不过如果真如阁下所说，这位发帖人只是在恶作剧的话，倒也无妨。.wav"
laikaen_prompt_text="不过如果真如阁下所说，这位发帖人只是在恶作剧的话，倒也无妨。"

    

def chat_with_content(content, refers_wav_path, prompt_text,audio_output_dir):
    # main infer params
    body = {
        "text": content,
        "refer_wav_path":refers_wav_path,
        "prompt_text":prompt_text,
        "prompt_language": "zh",
        "text_language": "zh"
    }

    print(body)

    try:
        response = requests.post(service_location, json=body)
        response.raise_for_status()
        # 读取响应内容
        content = response.content
        # 打开一个文件用于写入二进制数据
        wav_file = os.path.join(audio_output_dir, "1.wav")

        with open(wav_file, 'wb') as file:
            file.write(content)  # 将响应内容写入文件
        print(f"文件已保存到 {wav_file}")
        return wav_file

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")


def play_audio(content):
    tempfile = chat_with_content(content, ya_refer_wav_path,ya_prompt_text, audio_output_dir)
    if tempfile:
        # 直接播放已存在的文件
        os.system(f"ffplay -nodisp -autoexit {tempfile}")
        return tempfile
def gpt_sovit(text):
    return play_audio(text)
