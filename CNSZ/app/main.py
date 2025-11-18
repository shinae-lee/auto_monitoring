from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


## cors 에러

origins = [
    "http://localhost:5714",
    "http://127.0.0.1:5714",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"title": "myCNS FastAPI",
            "description": "Welcome to mySky FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}