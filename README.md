# yechani-TTS

## How To
0. 오디오 데이터 수집 및 분류
    - 라이브 방송 선정 후, `wav` 파일로 다운
    - `slient-divide.py`를 통해 파일 무음 기준으로 잘라서 편집(잡음이나 필요없는 음성 삭제 등)
    - 데이터 편집으로 인해 파일명이 1부터 시작하지만 중간에 빈 숫자가 있기 때문에 `rename-file-name.py`를 통해 파일명 재정의
    - `get-wav-length.py`를 통해 총 데이터의 시간 구할 수 있음
1. [Google Speech-to-Text API](https://cloud.google.com/speech-to-text)
    - 무료로 시작하기를 통해 API 사용 허가받기
2. [Google Cloud Platform](https://console.cloud.google.com/)
    - 구글 클라우드 플랫폼을 통해 프로젝트 생성
    - 메뉴에서 Cloud Storage 선택
    - 버킷 만들기
    - 버킷 안에 오디오 데이터 업로드
    - [구글 API키 인증 받기](https://cloud.google.com/docs/authentication/production)
        - `IAM 및 관리자` - `서비스 계정`
        - 서비스 계정 만들기
        - 서비스 계정 권한 - `소유자`
        - 서비스 계정 목록 - 작업 - `키 관리`
        - 키 추카 - 새 키 만들기 - `json`파일
        - json 파일이 자동으로 다운 되면, 해당 파일 경로 복사
        - `generate-script.py`가 있는 폴더에서 터미널 열기
        ```
        export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
        ```
        - 키 인증이 제대로 되었는지 확인하기 위해 `verify-auth.py` 실행
    - `generate-script.py`를 통해 스크립트 파일 생성
    - 스크립트 파일은 [tacotron](https://github.com/carpedm20/multi-Speaker-tacotron-tensorflow#2-1-generate-custom-datasets)에서 요구하는 json 형태로 생성
    - 생성된 스크립트 파일은 부정확할 수 있으니 확인 필요

## 내가 마주한 오류
- `Error: file does not start with RIFF id`    
    - [참고한 오류 해결법](https://stackoverflow.com/questions/50090404/error-file-does-not-start-with-riff-id)   
    유튜브 영상을 wav 파일로 다운받으면서 무언가 안 맞았는지, RIFF id 오류가 났다.    
    위의 오류 해결법을 사용하니 더 이상 에러가 나지 않았다.    
    하지만, 일일이 명령어를 칠 수 없었으니 이 또한 `RIFF-error.py`를 만들어 자동화를 했다.
- `ModuleNotFoundError: No module named 'pandas'`
    - anaconda3로 python 3.7를 설치하고 했음에도 이 오류가 떴다.
    - `pip3 install --upgrade pandas` 를 하면 재설치가 된다.
- `google.api_core.exceptions.InvalidArgument: 400 Request payload size exceeds the limit: 10485760 bytes.`
    - 구글 STT API 사용할 때, 로컬 파일로 스크립트 작성 중에 마주한 오류
    - [참고한 오류 해결법](https://st-yuri.medium.com/set-up-and-use-speech-to-text-api-in-python-78f1a0be167e)
    - 로컬 파일을 Google Cloud Platform에 업로드 후, 해당 경로를 통해 스크립트 파일을 만들면 된다.
- `google.api_core.exceptions.InvalidArgument: 400 Sync input too long. For audio longer than 1 min use LongRunningRecognize with a 'uri' parameter.`
    - 동기식 음성 인식을 이용할 경우 1분보다 긴 음성을 요청할 때, 이런 오류가 반환된다. [참조](https://cloud.google.com/speech-to-text/docs/error-messages)
    - [비동기 음성 인식](https://cloud.google.com/speech-to-text/docs/async-recognize)을 사용하여 반환하면 해결된다.
- [chldkato/Tacotron-Korean-Tensorflow2](https://github.com/chldkato/Tacotron-Korean-Tensorflow2) 코드 실행 시, `librosa` 등의 라이브러리 오류
    - M1 맥북으로 할 때, 파이썬 3.7은 아키텍쳐로 인해 깔리지 않는다는 여러 구글링을 통해, 파이썬 3.8은 되나? 싶어서 도전했더니 `pandas`오류인지를 만났다.
    - 결국엔 윈도우 데스크탑에 `anaconda3`로 파이썬3.7으로 맞춰주니 정상적으로 `preprocess.py`를 실행할 수 있었다.
## 참조
- DEVIEW 2017 김태훈님 발표
    - [영상](https://youtu.be/klnfWhPGPRs) 및 [PPT](https://www.slideshare.net/carpedm20/deview-2017-80824162)
    - [Tacotron 페이지](https://carpedm20.github.io/tacotron/)
    - [Github](https://github.com/carpedm20/multi-Speaker-tacotron-tensorflow)
- [Tacotron 한국어 가이드](https://github.com/GSByeon/multi-speaker-tacotron-tensorflow/blob/master/README_ko.md)
- [DJ You project](https://welcome-to-dewy-world.tistory.com/106?category=850079)
- [시리를 아이유 목소리로 바꾸기](https://blog.crux.cx/iu-siri-1/)
- https://hleecaster.com/google-cloud-speech-to-text-api/

## 사용 데이터
- [KSS dataset](https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset)

- [201108 인스타 라이브](https://youtu.be/TxSoAYf-diI)

- [210131 인스타 라이브](https://youtu.be/FIIBlRX2WHA)
- [210213 브이앱 라이브](https://www.vlive.tv/video/236796)
- [211206 인스타 라이브](https://youtu.be/ZIi28sEYrhE)
- [211212 인스타 라이브](https://youtu.be/d9GPc-VPvfI)

- [220116 인스타 라이브](https://youtu.be/NGjG2jA_xXM)
- [220126 인스타 라이브](https://youtu.be/zVq8L9NOsI4)
- [220206 인스타 라이브](https://youtu.be/-BD9NXSzKTw)
- [220227 인스타 라이브](https://youtu.be/NET4D6qniCI)