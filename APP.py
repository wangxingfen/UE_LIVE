import time
import os
import re
from ai_post.ai_imager import image_ai, talk_ai
from voice.gptsovits_service import gpt_sovit
import re
import pyautogui
import threading  # 添加线程模块

def handle_auto_request():
    """
    处理自动请求，监控屏幕变化
    """
    def move_action(keyboard,du):
        pyautogui.keyDown(keyboard)
        time.sleep(du)
        pyautogui.keyUp(keyboard)
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)
    #video_dir_path = "video_data/chuyin.mkv"
    asset_load_path = "video_data/cute"
    #data_preparation(video_dir_path,asset_load_path, True)
    img_path = "C:/Users/wangxingfeng/Pictures/render.png"
 
    while True:
        response = """"""
        try:
            if os.path.exists(img_path):
                # 保存截图
                #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                #img_path = f"./images/screenshot_{timestamp}.png"
                
                #pyautogui.screenshot(img_path)
                # 检查队列大小，如果队列任务接近完成，则运行 respose = talk_ai("")
                with open("./messages/user.txt", "r",encoding='utf-8') as f:
                    contents = f.read()
                contents="你的任务是找到跳舞的老鼠。"
                response = image_ai(contents,img_path)
                # 创建并启动线程来运行 extract_list
                thread = threading.Thread(target=extract_list, args=(response,))
                thread.start()
                if not os.path.exists("./messages/response.txt"):
                    with open("./messages/response.txt", "w",encoding='utf-8') as f:
                        f.write(response)
                        f.close()
                    #print(respose)
                    os.remove(img_path)
                os.remove("./messages/user.txt")

            else:
                time.sleep(1)
        except Exception as e:
            pass
def extract_list(text):
    # 修改正则表达式以提取列表而不是数字
        pattern = re.compile(r'\[(.*?)\]')
        result = []
        for match in pattern.finditer(text):
            if match.group(1):  # List format
                item = match.group(1)
                result.append([item.split(', ')[0], float(item.split(', ')[1])])
        print(result)

        for actions in list(result):
            key=actions[0]
            during=actions[1]
            pyautogui.keyDown(key)
            time.sleep(during)
            pyautogui.keyUp(key)

if __name__ == "__main__":
    handle_auto_request()
