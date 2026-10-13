from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Tracker API is running"}

@app.get("/about")
def about():
    return {"project": "Job Tracker", "version": "0.1"}

