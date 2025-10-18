from sqlalchemy import Column, Integer, Text
from app.database import Base

# Modelo de PokeFact (Estructura de la tabla poke_facts)
class PokeFact(Base):
    __tablename__ = "poke_facts"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, nullable=False)
    fact = Column(Text, nullable=False)
