from game_of_greed.game_of_greed import GameLogic

welcome_message = """
**************************************************
***                                            ***
***   Welcome to the Game of greed, have fun!   ***
***                                            ***
**************************************************
May the odds ever be in your favor! To start type: Start
"""

def start_game():
   response = input(welcome_message)
   input(welcome_message).lower == input(welcome_message).upper
   if response == str("Start"):
     run_game()

def run_game():
  while True:
    rolled_dice = GameLogic.roll_dice(6)

    if GameLogic.calculate_score(rolled_dice) == 0:
        print("Farkled")
        continue

start_game()
