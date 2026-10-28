from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABAE_URL = "postgresql://postgres:12345678901@localhost/blogdb"

engine = create_engine(DATABAE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()