import random
from agents import function_tool


@function_tool
def roll_dice(sides:int=6):
    """ it rolls a dice and generates the random number between 1 and sides """
    return random.randint(1,sides)