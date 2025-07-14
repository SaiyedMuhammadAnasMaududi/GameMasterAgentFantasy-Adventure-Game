from agents import function_tool
import random

@function_tool
def generate_event(context:str):
    """ Generates a radom event based on the the context """
    events = {
        "forest":["A goblin attacks!", "You find a treasure chest.", "You step into a trap!"],
        "village":["A merchant offers you a deal.", "You hear a rumor.", "A thief tries to steal from you."]
    }
    return random.choice(events.get[context,["nothing happens"]])