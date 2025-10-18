from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Leerlas.
USER = os.getenv("POSTGRES_USER", "admin123")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin123")
DB = os.getenv("POSTGRES_DB", "pokefact_db")
HOST = os.getenv("POSTGRES_HOST", "db")
PORT = os.getenv("POSTGRES_PORT", "5432")

# Crear la URL dinámica
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

# Crear motor y sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
