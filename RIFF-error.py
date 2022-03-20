import os
import subprocess

path_dir = '/Users/favorcat/Github/yechani-TTS/resource/output/' #경로 끝에 / 꼭 붙이기
file_list =os.listdir(path_dir) #경로 읽어 파일명 리스트 만들기
file_list.sort() #정렬

for file in file_list:
    command = "ffmpeg -i {} -acodec pcm_s16le -ac 1 -ar 16000 {}".format(os.path.join(path_dir,file), os.path.join(path_dir,"RIFF-ID/",file))
    subprocess.call(command, shell=True)