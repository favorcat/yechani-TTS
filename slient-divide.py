'''
* 참고 사이트 *
https://www.thetopsites.net/article/54596077.shtml
https://stackoverflow.com/questions/23730796/using-pydub-to-chop-up-a-long-audio-file
'''

# Import the AudioSegment class for processing audio and the 
# split_on_silence function for separating out silent chunks.
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

# Load your audio.
song = AudioSegment.from_wav("/Users/favorcat/Github/yechani-TTS/resource/210213.wav")

# Split track where the silence is 2 seconds or more and get chunks using 
# the imported function.
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
    chunk.export("/Users/favorcat/Github/yechani-TTS/resource/output/{0}.wav".format(i), format="wav")