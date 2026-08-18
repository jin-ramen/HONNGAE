from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

app = FastAPI()

@app.get("/")
def root(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        value = result.scalar()
        return {"status": "healthy", "database_response": value}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database unavailable: {str(e)}")