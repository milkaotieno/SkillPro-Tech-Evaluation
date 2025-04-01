from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SkillPro Tech API is running!"}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.post("/process")
def process_data(data: dict):
    return {"processed_data": data}


