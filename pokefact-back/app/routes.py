from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.model.pokefacts import PokeFact

# Crear el router
router = APIRouter(prefix="/api/v1", tags=["Facts"])

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@router.get("/facts")
def get_facts(db: Session = Depends(get_db)):
    return db.query(PokeFact).all()

@router.get("/facts/{pokemon_id}")
def get_fact(pokemon_id: int, db: Session = Depends(get_db)):
    fact = db.query(PokeFact).filter(PokeFact.pokemon_id == pokemon_id).first()
    if not fact:
        raise HTTPException(status_code=404, detail="Fact not found")
    return fact

@router.post("/facts")
def create_fact(pokemon_id: int, fact: str, db: Session = Depends(get_db)):
    new_fact = PokeFact(pokemon_id=pokemon_id, fact=fact)
    db.add(new_fact)
    db.commit()
    db.refresh(new_fact)
    return new_fact

@router.delete("/facts/{fact_id}")
def delete_fact(fact_id: int, db: Session = Depends(get_db)):
    fact = db.query(PokeFact).filter(PokeFact.id == fact_id).first()
    if not fact:
        raise HTTPException(status_code=404, detail="Fact not found")
    db.delete(fact)
    db.commit()
    return {"message": f"Fact with id {fact_id} deleted successfully"}
