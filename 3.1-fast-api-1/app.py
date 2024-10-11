from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Инициализация FastAPI
app = FastAPI()

# Инициализация базы данных (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./advertisements.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Модель объявления в базе данных
class Advertisement(Base):
    __tablename__ = "advertisements"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    author = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Создание таблицы в базе данных
Base.metadata.create_all(bind=engine)


# Модель данных для FastAPI
class AdvertisementCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    author: str


class AdvertisementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


# CRUD-операции

@app.post("/advertisement", response_model=dict)
def create_advertisement(advert: AdvertisementCreate):
    db = SessionLocal()
    new_advert = Advertisement(
        title=advert.title,
        description=advert.description,
        price=advert.price,
        author=advert.author,
    )
    db.add(new_advert)
    db.commit()
    db.refresh(new_advert)
    return {"id": new_advert.id}


@app.patch("/advertisement/{advertisement_id}", response_model=dict)
def update_advertisement(advertisement_id: int, advert: AdvertisementUpdate):
    db = SessionLocal()
    db_advert = db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()

    if not db_advert:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    if advert.title is not None:
        db_advert.title = advert.title
    if advert.description is not None:
        db_advert.description = advert.description
    if advert.price is not None:
        db_advert.price = advert.price

    db.commit()
    return {"message": "Advertisement updated successfully"}


@app.delete("/advertisement/{advertisement_id}", response_model=dict)
def delete_advertisement(advertisement_id: int):
    db = SessionLocal()
    db_advert = db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()

    if not db_advert:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    db.delete(db_advert)
    db.commit()
    return {"message": "Advertisement deleted successfully"}


@app.get("/advertisement/{advertisement_id}", response_model=dict)
def get_advertisement(advertisement_id: int):
    db = SessionLocal()
    advert = db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()

    if not advert:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    return {
        "id": advert.id,
        "title": advert.title,
        "description": advert.description,
        "price": advert.price,
        "author": advert.author,
        "created_at": advert.created_at,
    }


@app.get("/advertisement", response_model=List[dict])
def search_advertisements(title: Optional[str] = None, author: Optional[str] = None):
    db = SessionLocal()
    query = db.query(Advertisement)

    if title:
        query = query.filter(Advertisement.title.contains(title))
    if author:
        query = query.filter(Advertisement.author == author)

    adverts = query.all()

    return [
        {
            "id": advert.id,
            "title": advert.title,
            "description": advert.description,
            "price": advert.price,
            "author": advert.author,
            "created_at": advert.created_at,
        } for advert in adverts
    ]
