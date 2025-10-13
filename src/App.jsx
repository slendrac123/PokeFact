import { useState } from "react";

function App() {
  const [pokemon, setPokemon] = useState(null);
  const [search, setSearch] = useState("");

  const handleSearch = async () => {
    if (!search) return;

    try {
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${search.toLowerCase()}`);
      if (!response.ok) {
        throw new Error("Pokémon no encontrado");
      }

      const data = await response.json();
      setPokemon(data);
    } catch (error) {
      console.error(error);
      setPokemon(null);
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
          placeholder="¿Que Pokémon buscas?"
          className="px-3 py-2 rounded-lg text-white"
        />
        <button
          onClick={handleSearch}
          className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded-lg"
        >
          Buscar
        </button>
      </div>

      {pokemon && (
        <div className="text-center bg-slate-800 p-4 rounded-lg shadow-lg">
          <img
            src={pokemon.sprites.front_default}
            alt={pokemon.name}
            className="mx-auto w-32 h-32"
          />
          <h2 className="text-2xl capitalize font-semibold mt-2">
            {pokemon.name}
          </h2>
          <p>Altura: {pokemon.height}</p>
          <p>Peso: {pokemon.weight}</p>
          <p>Tipo: {pokemon.types.map((t) => t.type.name).join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
