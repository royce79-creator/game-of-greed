from game_of_greed.game_logic import GameLogic

welcome_message = """
**************************************************
***                                            ***
***   Welcome to the Game of greed, have fun!   ***
***                                            ***
**************************************************
May the odds ever be in your favor! To start type: Start. If not type "quit" to exit. 
"""
# Want to prompt the user to start making a choise with either starting or quitting using available options "start" or "quit"


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


if __name__ == '__main__':
start_game()
run_game()
