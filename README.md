### 가상환경 생성
python -m venv .venv

### 가상환경 실행
source ./.venv/Scripts/activate

### 패키지 설치
pip install -r requirements.txt

### fast api 서버 실행
uvicorn app.main:app (--reload)

### vue 서버 실행
npm run dev
