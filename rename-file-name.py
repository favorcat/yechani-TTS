import os

count = 0
dir = "/Users/favorcat/Github/yechani-TTS/resource/output"
for file in os.listdir(dir):
    count+=1
    file_oldname = os.path.join(dir, file)
    file_newname_newfile = os.path.join(dir, str(count)+".wav")
    os.rename(file_oldname, file_newname_newfile)