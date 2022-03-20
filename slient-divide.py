'''
* 참고 사이트 *
https://www.thetopsites.net/article/54596077.shtml
https://stackoverflow.com/questions/23730796/using-pydub-to-chop-up-a-long-audio-file
'''

import os
# Import the AudioSegment class for processing audio and the 
# split_on_silence function for separating out silent chunks.
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

path_dir = '/Users/favorcat/Github/yechani-TTS/resource/' #경로 끝에 / 꼭 붙이기
folder_list = os.listdir(path_dir) #경로 읽어 여러 폴더들 읽기
folder_list.sort() #정렬

for folder in folder_list:
    if (folder != '.DS_Store'):
        folder_dir = os.path.join(path_dir,folder)
        file_name = "{}.wav".format(folder)
        file_dir = os.path.join(folder_dir,file_name)

        # Load your audio.
        song = AudioSegment.from_wav(file_dir)
        print(file_dir)

        chunks = split_on_silence (
            # Use the loaded audio.
            song, 
            # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
            min_silence_len = 400,
            # Consider a chunk silent if it's quieter than -16 dBFS.
            # (You may want to adjust this parameter.)
            silence_thresh = -40
        )

        # Process each chunk with your parameters
        for i, chunk in enumerate(chunks):
            print("chunk >> ", i)
            # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
            silence_chunk = AudioSegment.silent(duration=100)
            # Add the padding chunk to beginning and end of the entire chunk.
            audio_chunk = silence_chunk + chunk + silence_chunk
            # Normalize the entire chunk.
            normalized_chunk = match_target_amplitude(audio_chunk, -20.0)
            # Export the audio chunk with new bitrate.
            chunk.export("{0}/output/{1}.wav".format(folder_dir,i), format="wav")