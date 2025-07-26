
from agents import Agent,OpenAIChatCompletionsModel,set_tracing_disabled
from client.openai_client import client
set_tracing_disabled(True)
class ItemAgent(Agent):
    def __init__(self):
        super().__init__(name="Item",instructions="You handle items found in the game. When a player finds an item, you add it to their inventory." ,model=OpenAIChatCompletionsModel(openai_client=client,model="gemini-2.0-flash"))
    async def call(self, input_text, context):
        context.context.setdefault("inventory", []).append("Gold Coin")
        context.context["next_agent"] = "Narrator"
        return "You open the chest and find a Gold Coin! It's added to your inventory."
