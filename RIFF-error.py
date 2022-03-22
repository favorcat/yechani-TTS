import os
import subprocess

path_dir = '/Users/favorcat/Github/yechani-TTS/resource/' #경로 끝에 / 꼭 붙이기
folder_list = os.listdir(path_dir) #경로 읽어 여러 폴더들 읽기
folder_list.sort() #정렬

for folder in folder_list:
    if (folder != '.DS_Store'):
        output_dir = os.path.join(path_dir,folder,'output/')
        file_list = os.listdir(output_dir)
        file_list.sort()
        
        for file in file_list:
            command = "ffmpeg -i {} -acodec pcm_s16le -ac 1 -ar 16000 {}".format(os.path.join(output_dir,file), os.path.join(path_dir,folder,"RIFF-ID/",file))
            subprocess.call(command, shell=True)