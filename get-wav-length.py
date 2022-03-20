# https://dolhani.tistory.com/540 참조

import os
import wave

def get_duration(audio_path):
    audio = wave.open(audio_path, 'rb')
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames / float(rate)
    return duration

path_dir = '/Users/favorcat/Github/yechani-TTS/resource/output/RIFF-ID/' #경로 끝에 / 꼭 붙이기
file_list =os.listdir(path_dir) #경로 읽어 파일명 리스트 만들기
file_list.sort() #정렬

res = 0
for file in file_list:
    path = path_dir+file
    res += get_duration(path)

sec = res % 60
min = int(res / 60 % 60)
print(sec , 'sec')
print(min, 'min', sec , 'sec')