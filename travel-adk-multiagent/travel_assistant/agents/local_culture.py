from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import recommend_local_culture

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.5-flash",
    description="Recommends local food, customs and useful travel phrases.",
    instruction="""
You are a local culture advisor for travelers.
Your task is to recommend typical food, relevant customs and useful phrases.

Rules:
1. Be practical.
2. Avoid stereotypes.
3. Explain why each recommendation matters to a traveler.
4. Use the available tool when a destination is provided.
5. Answer in Spanish.
""",
    tools=[recommend_local_culture],
)