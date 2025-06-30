from moviepy.editor import VideoFileClip
import imageio

def extract_last_frame_moviepy(video_path, output_path="last_frame.png"):
    # 加载视频并获取总时长
    clip = VideoFileClip(video_path)
    duration = clip.duration

    # 提取最后一帧（时间接近末尾，避免超出范围）
    last_frame = clip.get_frame(duration - 0.01)  # 减去微小偏移量

    # 保存为图片
    imageio.imwrite(output_path, last_frame)
    print(f"最后一帧已保存至 {output_path}")

# 示例调用
extract_last_frame_moviepy("input.mp4")