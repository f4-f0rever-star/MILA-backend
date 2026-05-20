const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

export async function getCultures() {
  try {
    const response = await fetch(`${API_URL}/cultures`);

    if (!response.ok) {
      throw new Error("Failed to fetch cultures");
    }

    return await response.json();
  } catch (error) {
    console.error("API Error:", error);
    return [];
  }
}

export async function getCultureById(id) {
  try {
    const response = await fetch(`${API_URL}/cultures/${id}`);

    if (!response.ok) {
      throw new Error("Failed to fetch culture");
    }

    return await response.json();
  } catch (error) {
    console.error("API Error:", error);
    return null;
  }
}