import os
import asyncio

from agent.items_agent import ItemAgent
from agent.monster_agent import MonsterAgent
from agent.narrator_agent import NarratorAgent
from context.game_context import GameContext

from agents import Runner
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")



async def main():
    context=GameContext()
    agents={
        "Narrator":NarratorAgent(),
        "Monster":MonsterAgent(),
        "Item":ItemAgent()
    }
    runner=Runner()

    current_agent=agents["Narrator"]

    print("🎮🎮Welcome to the Fantasy Adventure Game!\n")
    input_text = ""

    while True:
        result = await runner.run(current_agent, input_text, context=context)
        print(f"\n{result.final_output}")

        input_text = input("\n💬 Your choice: ")

        next_agent_name = context.context.get("next_agent", "Narrator")
        current_agent = agents.get(next_agent_name, current_agent)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
