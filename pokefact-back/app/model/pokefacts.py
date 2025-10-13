from pydantic import BaseModel

class PokeFact(BaseModel):
    id: int
    pokemon_id: int
    fact: str