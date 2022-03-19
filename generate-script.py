def transcribe_gcs(gcs_uri):
    from google.cloud import speech

    client = speech.SpeechClient()

    # wav 파일이라 2채널 오디오
    # https://cloud.google.com/speech-to-text/docs/multi-channel 참조
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code='ko-KR',
        audio_channel_count=2,
        enable_separate_recognition_per_channel=False)

    response = client.recognize(config=config, audio=audio)
    
    # json 파일에 내용추가
    with open("/Users/favorcat/Github/yechani-TTS/script.json", "a") as script:
        for result in response.results:
            print('"'+gcs_uri+'": "'+u'{}'.format(result.alternatives[0].transcript)+'",')
            script.write('"'+gcs_uri+'": "'+u'{}'.format(result.alternatives[0].transcript)+'",\n')
cnt = 104
while(cnt <= 783):
    # gs://~ 는 버킷 내부의 오디오 데이터 경로
    transcribe_gcs("gs://speechtotext-yechani/210213/"+str(cnt)+".wav")
    cnt+=1
    
# 오류 발생시 https://cloud.google.com/speech-to-text/docs/error-messages 참조