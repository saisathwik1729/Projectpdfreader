from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class PDFMeta(Base):
    _tablename_ = "pdfs"

    filename = Column(String, primary_key=True, index=True)
    upload_time = Column(DateTime, default=datetime.utcnow)