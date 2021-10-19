
from fastapi import FastAPI
from publication import publicationController

app = FastAPI()
app.include_router(publicationController.router)
sleep_time = 10

@app.get("/")
def root():
    return {
        "message": "/"
    }