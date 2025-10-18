from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import router as facts_router

# Crear la aplicación FastAPI
app = FastAPI()

#Cors para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)


# Incluir las rutas desde routes.py
app.include_router(facts_router)