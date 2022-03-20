def transcribe_file(speech_file):
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
    with open("/Users/favorcat/Github/yechani-TTS/script-local.json", "a") as script:
        for result in response.results:
            print('"'+speech_file+'": "'+u'{}'.format(result.alternatives[0].transcript)+'",')
            script.write('"'+speech_file+'": "'+u'{}'.format(result.alternatives[0].transcript)+'",\n')
cnt = 530
while(cnt <= 783):
    # gs://~ 는 버킷 내부의 오디오 데이터 경로
    transcribe_file("/Users/favorcat/Github/yechani-TTS/resource/output/"+str(cnt)+".wav")
    cnt+=1
    
# 오류 발생시 https://cloud.google.com/speech-to-text/docs/error-messages 참조