from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API is running"}


@app.get("/healthy")
def healthy():
    return {"message": "healthy"}


@app.get("/me")
def me():
    return {
        "name": "Okpunor Emmanuel",
        "email": "okpunorrex@gmail.com",
        "github": "https://github.com/okp980",
    }
