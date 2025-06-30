import time
import os
import re
from ai_post.ai_talker import ai_talker
from voice.gptsovits_service import gpt_sovit
import cv2  # 新增：引入 OpenCV 库

def handle_auto_request():
    """
    处理自动请求，监控屏幕变化
    """
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)
    asset_load_path = "video_data/cute"
    img_path = "C:/Users/wangxingfeng/Pictures/render.png"
 
    while True:
        respose = ""
        try:
            '''
            if os.path.exists(img_path):
                # 使用 OpenCV 处理图像
                img = cv2.imread(img_path)  # 读取图像
                if img is not None:
                    # 调整图像大小
                    img = cv2.resize(img, (640, 480))  # 调整为较小尺寸
                    # 转换为灰度图像
                    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # 应用高斯模糊
                    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
                    # 保存预处理后的图像
                    temp_img_path = "processed_render.png"
                    cv2.imwrite(temp_img_path, img_blur)'''
                    
                    # 使用预处理后的图像进行 AI 处理
            with open("messages/user.txt", "r", encoding='utf-8') as f:
                contents = f.read()
            if not os.path.exists("messages/response.txt"):
                respose = ai_talker(contents)  # 使用预处理后的图像路径
                print(respose)
                '''
                nums = re.findall(r'([-+]?\d*\.\d+|\d+)', respose)
                left_right = nums[0]
                ahead_behind = nums[1]
                duration=nums[2]'''
                if not os.path.exists("messages/response.txt"):
                    with open("./messages/response.txt", "w", encoding='utf-8') as f:
                        f.write(respose)
                    os.remove(img_path)
                os.remove("messages/user.txt")
                
                # 删除临时文件

        except Exception as e:
            pass

if __name__ == "__main__":
    handle_auto_request()