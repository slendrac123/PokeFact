import { useState } from "react";

function App() {
  const [pokemon, setPokemon] = useState(null);
  const [search, setSearch] = useState("");
  const [fact, setFact] = useState("");

  const handleSearch = async () => {
    if (!search.trim()) return; // 👈 evita búsquedas vacías o con solo espacios

    try {
      // 🔹 1. Buscar Pokémon en la PokeAPI
      const response = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${search.toLowerCase()}`
      );

      if (!response.ok) {
        throw new Error("Pokémon no encontrado");
      }

      const data = await response.json();
      setPokemon(data);

      // 🔹 2. Buscar el fact en backend
      const factResponse = await fetch(
        `http://localhost:8000/api/v1/facts/${data.id}`
      );

      if (factResponse.ok) {
        const factData = await factResponse.json();
        // 👇 verifica que tenga el campo "fact"
        setFact(factData.fact || "Fact vacío en la base de datos.");
      } else {
        setFact("No hay facts para este Pokémon.");
      }
    } catch (error) {
      console.error("Error al buscar Pokémon o fact:", error);
      setPokemon(null);
      setFact("");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-slate-900 text-white p-4">
      <h1 className="text-3xl font-bold mb-6">🔍 PokeFact</h1>

      <div className="flex gap-2 mb-6">
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="¿Qué Pokémon buscas?"
          className="px-3 py-2 rounded-lg text-black" // 👈 texto negro sobre fondo claro
        />
        <button
          onClick={handleSearch}
          className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded-lg"
        >
          Buscar
        </button>
      </div>

      {pokemon && (
        <div className="text-center bg-slate-800 p-4 rounded-lg shadow-lg max-w-xs">
          <img
            src={pokemon.sprites?.front_default}
            alt={pokemon.name}
            className="mx-auto w-32 h-32"
          />
          <h2 className="text-2xl capitalize font-semibold mt-2">
            {pokemon.id+" - "+pokemon.name}
          </h2>
          <p>Altura: {pokemon.height}</p>
          <p>Peso: {pokemon.weight}</p>
          <p>Tipo: {pokemon.types.map((t) => t.type.name).join(", ")}</p>
          <p className="mt-2">
            <strong>Fact:</strong> {fact}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
