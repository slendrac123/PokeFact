CREATE TABLE IF NOT EXISTS poke_facts (
    id SERIAL PRIMARY KEY,
    pokemon_id INT NOT NULL,
    fact TEXT NOT NULL
);

INSERT INTO poke_facts (pokemon_id, fact)
VALUES 
  (1, 'Bulbasaur lleva una semilla que crece con él.'),
  (4, 'Charmander tiene una llama en la cola que indica su estado de salud.'),
  (6, 'Charizard no es un dragón :( al menos no sin Mega.'),
  (7, 'Squirtle puede retraer su cabeza y extremidades en su caparazón.'),
  (25, 'Pikachu. Siempre Pikachu.'),
  (39, 'Jigglypuff puede hacer que los oponentes se duerman cantando.'),
  (52, 'Meowth puede caminar sobre dos patas.'),
  (65, 'Alakazam tiene un IQ de 5000.'),
  (94, 'Favorito de muchos.'),
  (94, 'Gengar podria ser la sombra de Clefable.'),
  (143, 'Snorlax puede comer más de 900 libras de comida en un solo día.'),
  (150, 'Mewtwo es un clon de Mew.'),
  (497, 'Un pokémon de tipo SSS. Simple Superior Serpent.');
  
  
