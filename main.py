from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index_page():
    return {'data': {'name': 'Alex'}}


@app.get("/about")
def info_page():
    return {'page_data': {'name': 'for test'}}