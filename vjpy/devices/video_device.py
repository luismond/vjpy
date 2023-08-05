"""vjpy video writer."""

from moviepy.editor import VideoFileClip, CompositeVideoClip

VIDEO_NAME = ""
VIDEO = VideoFileClip(VIDEO_NAME).subclip(0, 2)
result = CompositeVideoClip([VIDEO])
result.write_videofile(f"{VIDEO_NAME}_test.webm", fps=10)
