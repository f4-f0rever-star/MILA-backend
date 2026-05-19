import { useEffect, useState } from "react";
import { getCultures } from "./services/cultureApi";

function App() {
  const [cultures, setCultures] = useState([]);
  const [selectedCulture, setSelectedCulture] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadCultures() {
      const data = await getCultures();
      setCultures(data);
      setLoading(false);
    }

    loadCultures();
  }, []);

  if (loading) {
    return <h2>Loading cultures...</h2>;
  }

  return (
    <main>
      <h1>Culture Explorer</h1>

      <section>
        <h2>Explore Cultures</h2>

        {cultures.map((culture) => (
          <button
            key={culture.id}
            onClick={() => setSelectedCulture(culture)}
          >
            {culture.name}
          </button>
        ))}
      </section>

      {selectedCulture && (
        <section>
          <h2>{selectedCulture.name}</h2>
          <p>{selectedCulture.description}</p>

          <h3>Food</h3>
          <ul>
            {selectedCulture.foods.map((food) => (
              <li key={food}>{food}</li>
            ))}
          </ul>

          <h3>Traditions</h3>
          <ul>
            {selectedCulture.traditions.map((tradition) => (
              <li key={tradition}>{tradition}</li>
            ))}
          </ul>
        </section>
      )}
    </main>
  );
}

export default App;