from fastapi import FastAPI
from database.db import SessionLocal
from sqlalchemy import text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/test-db")
def test_db():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"message": "Database Connected Successfully ✅"}
    except Exception as e:
        return {"error": str(e)}