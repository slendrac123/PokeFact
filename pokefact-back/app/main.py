from fastapi import FastAPI, HTTPException
from  app.model.pokefacts import PokeFact
from fastapi.middleware.cors import CORSMiddleware

pokefact_db = [
    {
        "id": 1,
        "pokemon_id": 1,
        "fact": "Bulbasaur can be seen napping in bright sunlight."
    },
    {
        "id": 4,
        "pokemon_id": 4,
        "fact": "Charmander prefers hot things. When it rains, steam is said to spout from the tip of its tail."
    },
    {
        "id": 7,
        "pokemon_id": 7,
        "fact": "Squirtle's shell is not merely used for protection. The shell's rounded shape and the grooves on its surface help minimize resistance in water, enabling this Pokémon to swim at high speeds."
    },
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, PokeFact!"}

@app.get("/api/v1/facts", response_model=list[PokeFact])
def get_facts():
    return pokefact_db

@app.get("/api/v1/facts/{pokemon_id}", response_model=PokeFact)
def get_fact(pokemon_id: int):
    for fact in pokefact_db:
        if fact["pokemon_id"] == pokemon_id:
            return fact
    raise HTTPException(status_code=404, detail="Fact not found")

@app.post("/api/v1/facts", response_model=PokeFact)
def create_fact(fact_data: PokeFact):
    new_fact = fact_data.model_dump()
    pokefact_db.append(new_fact)
    return new_fact

@app.delete("/api/v1/facts/{fact_id}", response_model=PokeFact)
def delete_fact(fact_id: int):
    for fact in pokefact_db:
        if fact["id"] == fact_id:
            fact_deleted = fact
            pokefact_db.remove(fact)
            return fact_deleted
    raise HTTPException(status_code=404, detail="Fact not found")

#models.Base.metadata.create_all(bind=database.engine)


#app.include_router(routes.router)