def recommend_local_culture(destination: str) -> dict:
    """Recommend basic local culture information for a destination."""
    destination_normalized = destination.lower().strip()

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        return {
            "status": "success",
            "destination": destination,
            "foods": ["cuy al horno", "chiri uchu", "sopa de quinua"],
            "customs": [
                "Respect archaeological sites and marked routes.",
                "Ask before photographing local people.",
                "Move slowly during the first day because of altitude.",
            ],
            "phrases": ["Buenos días", "Gracias", "¿Cuánto cuesta?", "¿Dónde queda...?"],
        }

    if "buenos aires" in destination_normalized:
        return {
            "status": "success",
            "destination": destination,
            "foods": ["empanadas", "asado", "milanesa", "alfajores"],
            "customs": [
                "Dinner is commonly later than in many other countries.",
                "Public transport usually requires a SUBE card.",
                "Neighborhood identity is strong; plan by zones.",
            ],
            "phrases": ["Hola", "Gracias", "¿Cuánto sale?", "¿Dónde queda...?"],
        }

    return {
        "status": "success",
        "destination": destination,
        "foods": ["Typical local dishes should be verified for the destination."],
        "customs": ["Check local etiquette, schedules and public transport habits."],
        "phrases": ["Hello", "Thank you", "How much is it?", "Where is...?"],
    }