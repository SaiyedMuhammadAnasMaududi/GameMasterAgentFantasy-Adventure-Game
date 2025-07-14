
from agents import Agent

class ItemAgent(Agent):
    def __init__(self):
        super().__init__(name="Item",instructions="You handle items found in the game. When a player finds an item, you add it to their inventory." )
    async def call(self, input_text, context):
        context.context.setdefault("inventory", []).append("Gold Coin")
        context.context["next_agent"] = "Narrator"
        return "You open the chest and find a Gold Coin! It's added to your inventory."
