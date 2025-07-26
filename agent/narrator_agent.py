from agents import Agent,OpenAIChatCompletionsModel,set_tracing_disabled
from tools.events_tool import generate_event
from client.openai_client import client
set_tracing_disabled(True)
class NarratorAgent(Agent):
    def __init__(self):
        super().__init__(name="Narrator", instructions="You narrate the story and guide the player through their adventure. You generate events based on the player's actions.",model=OpenAIChatCompletionsModel(openai_client=client,model="gemini-2.0-flash"))

    def call(self,input_text,context):
         
         if "forest" in input_text:
              event= generate_event("forest")
              if "goblin" in event:
                   context.context["next-agent"]="Monster"
              elif "treasure" in event:
                   context.context["next-agent"]="Item"
                   return f"You are in a forest. {event} What do you want to do next?"  
         elif "village" in input_text:
                event= generate_event("village")
                if "merchant" in event:
                     context.context["next-agent"]="Merchant"
                elif "thief" in event:
                     context.context["next-agent"]="Thief"
                     return f"You are in a village. {event} What do you want to do next?"
         else:
              return"You start your journey. Do you want to go to the forest or the village?"         