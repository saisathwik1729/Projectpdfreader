from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime

# Base class for SQLAlchemy models
Base = declarative_base()

# PDF metadata table
class PDFMeta(Base):
    __tablename__ = 'pdf_metadata'  # <-- corrected double underscores

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    pages = Column(Integer)
    upload_time = Column(DateTime, default=datetime.utcnow)

# SQLite database URL (you can change this to PostgreSQL if needed)
DATABASE_URL = "sqlite:///./pdfs.db"

# Database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

# Save metadata function
def save_metadata(db: Session, filename: str, pages: int):
    metadata = PDFMeta(filename=filename, pages=pages)
    db.add(metadata)
    db.commit()
    db.refresh(metadata)
    return metadata
