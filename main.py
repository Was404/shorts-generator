from moviepy.editor import *
import os
from config import *

files = os.listdir(DIRECTORY)
images = list(filter(lambda x: x.endswith('.jpg'), files))


#Создаем слайдшоу из изображений
#image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]
clips = [ImageClip(m).set_duration(TIME_IMAGE) for m in images]
video = concatenate_videoclips(clips, method="compose")

#Добавляем текст
txt_clip = TextClip("My Slideshow", fontsize=70, color='white')
txt_clip = txt_clip.set_position('center').set_duration(6)
video = CompositeVideoClip([video, txt_clip])

#Добавляем музыку
audio = AudioFileClip("background_music.mp3")
video = video.set_audio(audio)

#Сохраняем результат
video.write_videofile("slideshow.mp4", fps=24)