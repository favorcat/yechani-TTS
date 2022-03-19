# yechani-TTS
---

### How To
0. 오디오 데이터 수집 및 분류
    - 라이브 방송 선정 후, `wav` 파일로 다운
    - `slient-divide.py`를 통해 파일 무음 기준으로 잘라서 편집(잡음이나 필요없는 음성 삭제 등)
    - 데이터 편집으로 인해 파일명이 1부터 시작하지만 중간에 빈 숫자가 있기 때문에 `rename-file-name.py`를 통해 파일명 재정의
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


## 참조
- DEVIEW 2017 김태훈님 발표
    - [영상](https://youtu.be/klnfWhPGPRs) 및 [PPT](https://www.slideshare.net/carpedm20/deview-2017-80824162)
    - [Tacotron 페이지](https://carpedm20.github.io/tacotron/)
    - [Github](https://github.com/carpedm20/multi-Speaker-tacotron-tensorflow)
- [Tacotron 한국어 가이드](https://github.com/GSByeon/multi-speaker-tacotron-tensorflow/blob/master/README_ko.md)
- [DJ You project](https://welcome-to-dewy-world.tistory.com/106?category=850079)
- [시리를 아이유 목소리로 바꾸기](https://blog.crux.cx/iu-siri-1/)
- https://hleecaster.com/google-cloud-speech-to-text-api/