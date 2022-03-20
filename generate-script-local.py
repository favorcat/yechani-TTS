import os

def transcribe_file(dir, speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    # wav 파일이라 2채널 오디오
    # https://cloud.google.com/speech-to-text/docs/multi-channel 참조
    # https://cloud.google.com/speech-to-text/docs/sync-recognize 참조

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code='ko-KR',
        audio_channel_count=2,
        enable_separate_recognition_per_channel=False)

    response = client.recognize(config=config, audio=audio)
    
    # json 파일에 내용추가
    with open(dir+"/script-local.json", "a") as script:
        for result in response.results:
            print('"'+speech_file+'": "'+u'{}'.format(result.alternatives[0].transcript)+'",')
            script.write('"'+speech_file+'": "'+u'{}'.format(result.alternatives[0].transcript)+'",\n')
            

path_dir = '/Users/favorcat/Github/yechani-TTS/resource/' #경로 끝에 / 꼭 붙이기
folder_list = os.listdir(path_dir) #경로 읽어 여러 폴더들 읽기
folder_list.sort() #정렬

for folder in folder_list:
    if (folder != '.DS_Store' and folder != '210213 - 완료'):
        folder_dir = os.path.join(path_dir,folder)
        output_dir = os.path.join(folder_dir,'output/')
        
        file_list = os.listdir(output_dir)
        file_len = len(file_list)

        for i in range(file_len) :
            # gs://~ 는 버킷 내부의 오디오 데이터 경로
            transcribe_file(folder_dir, output_dir+str(i)+".wav")
    
# 오류 발생시 https://cloud.google.com/speech-to-text/docs/error-messages 참조