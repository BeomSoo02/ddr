# MOVE AI · 길새김 Streamlit 앱

기존 독립형 HTML 프로토타입을 Streamlit에서 실행하고 배포할 수 있도록 구성한 버전입니다.
원본의 화면, CSS, JavaScript, 이미지, 시연 흐름을 하나의 HTML 컴포넌트 안에 보존합니다.

## 로컬 실행

Python 3.10 이상을 권장합니다.

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

브라우저에서 자동으로 열리지 않으면 터미널에 표시되는 주소(기본값 `http://localhost:8501`)로 접속합니다.

## Streamlit Community Cloud 배포

1. 이 폴더의 파일을 GitHub 저장소에 올립니다.
2. Streamlit Community Cloud에서 **Create app**을 선택합니다.
3. 저장소와 브랜치를 선택하고 Main file path에 `app.py`를 입력합니다.
4. **Deploy**를 누릅니다. 별도의 Secrets 설정은 필요하지 않습니다.

## 구성

- `app.py`: Streamlit 진입점
- `gilsaegim-standalone.html`: 기존 UI와 자산이 포함된 독립형 화면
- `requirements.txt`: 배포용 Python 의존성
- `.streamlit/config.toml`: 서버 및 테마 설정

## 참고

- 핵심 시연은 브라우저 폴백 데이터로 동작하므로 별도 API 서버 없이 배포할 수 있습니다.
- 사진 선택과 음성 녹음은 브라우저 권한 및 iframe 보안 정책의 영향을 받을 수 있습니다. 권한을 사용할 수 없으면 기존 예시 미디어 폴백이 동작합니다.
- Streamlit 앱을 새로고침하면 HTML 프로토타입의 현재 화면 상태도 초기화됩니다.

