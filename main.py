
from fastapi import FastAPI
from publication import publicationController
from author import authorController, authorshipController
from paper import paperController

app = FastAPI()
app.include_router(publicationController.router)
app.include_router(authorController.router)
app.include_router(authorshipController.router)
app.include_router(paperController.router)
sleep_time = 10

@app.get("/")
def root():
    return {
        "message": "/"
    }