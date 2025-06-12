from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from utils import process_pdf, answer_question
from database import save_metadata
import shutil
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = process_pdf(file_location)
    save_metadata(file.filename)
    return {"filename": file.filename, "text": text[:200]}

@app.post("/ask")
async def ask_question_api(filename: str = Form(...), question: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, filename)
    answer = answer_question(file_path, question)
    return {"answer": answer}