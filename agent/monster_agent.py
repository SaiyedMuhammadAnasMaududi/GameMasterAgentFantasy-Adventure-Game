from agents import Agent
from tools.dice_tool import roll_dice


class MonsterAgent(Agent):
    def __init__(self):
        super().__init__(name="Monster",instructions = (
        "You handle combat when a monster appears using a dice tool. "
        "If the number is greater than 10, you defeat the monster. Otherwise, "
        "the monster wins and the story begins from the start."
    ))
    

    def call(self, input_text, context):
        var = "start"  # Any non-empty string to start the loop

        while var != "":
            dice_roll = roll_dice(20)

            if dice_roll > 10:
                var=""
                context.context["next-agent"] = "Narrator"
                return f"You swing your sword and roll {dice_roll}. It's a hit! The goblin is defeated!"
            else:
                print(f"You swing your sword and roll {dice_roll}. The goblin dodges your attack and strikes back! You lose the fight. The story will begin from the start.")
                var = input("To try again, write anything (or just press Enter to quit): ")

        return "You chose to end the battle. The story ends here... for now."
