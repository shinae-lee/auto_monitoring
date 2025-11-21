from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


## cors 에러

# origins = [
#     "http://localhost:5717"
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"title": "myCNS FastAPI",
            "description": "Welcome to mySky FastAPI application!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "backend-python"}