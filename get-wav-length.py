# https://dolhani.tistory.com/540 참조

import os
import wave

def get_duration(audio_path):
    audio = wave.open(audio_path, 'rb')
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames / float(rate)
    return duration

path_dir = '/Users/favorcat/Github/yechani-TTS/resource/' #경로 끝에 / 꼭 붙이기
folder_list = os.listdir(path_dir) #경로 읽어 여러 폴더들 읽기
folder_list.sort() #정렬

res = 0
for folder in folder_list:
    if (folder != '.DS_Store'):
        output_dir = os.path.join(path_dir,folder,'output/')
        file_list = os.listdir(output_dir)
        file_list.sort()

        for file in file_list:
            path = output_dir+file
            res += get_duration(path)

sec = res % 60
min = int(res / 60 % 60)
print(sec , 'sec')
print(min, 'min', sec , 'sec')