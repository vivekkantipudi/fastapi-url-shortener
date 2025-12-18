import string
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
import database, models

# Initialize Database Tables automatically
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

class URLCreate(BaseModel):
    original_url: str

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_short_code(id_num: int) -> str:
    characters = string.digits + string.ascii_letters
    id_num += 100000000 # Ensures a 6-character string
    base62 = []
    while id_num > 0:
        id_num, rem = divmod(id_num, 62)
        base62.append(characters[rem])
    return "".join(reversed(base62))

@app.post("/api/shorten")
def shorten_url(item: URLCreate, db: Session = Depends(get_db)):
    db_url = models.URL(original_url=item.original_url, short_code="")
    db.add(db_url)
    db.commit()
    
    code = generate_short_code(db_url.id)
    db_url.short_code = code
    db.commit()
    return {"short_code": code, "original_url": item.original_url}

@app.get("/{short_code}")
def redirect_to_url(short_code: str, request: Request, db: Session = Depends(get_db)):
    url_record = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Not Found")
    
    new_click = models.Click(
        url_id=url_record.id,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    db.add(new_click)
    db.commit()
    return RedirectResponse(url=url_record.original_url, status_code=302)

@app.get("/api/stats/{short_code}")
def get_stats(short_code: str, db: Session = Depends(get_db)):
    url_record = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Not Found")
    
    count = db.query(models.Click).filter(models.Click.url_id == url_record.id).count()
    return {"short_code": short_code, "total_clicks": count}