from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
import sys

welcome_message = """
**************************************************
***                                            ***
***   Welcome to the Game of greed, have fun!   ***
***                                            ***
**************************************************
May the odds ever be in your favor! To start type: Start. If not type "quit" to exit. 
"""
# Want to prompt the user to start making a choise with either starting or quitting using available options "start" or "quit"

class Game: 
  def __init__(self):
    self.round_counter = 0
    self.dice_amount = 6
    self.banker = Banker()
  
  def main_roller(self):
    GameLogic.roll_dice(self.dice_amount)

  def play(self, roller = GameLogic.roll_dice):
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    response = input('> ')

    if response == 'n':
      print('OK. Maybe another time')
    elif response == 'y':
      self.run_game(roller)
  
  def run_game(self, roller):

    while True:
      self.round_counter += 1

      print(f'Starting round {self.round_counter}')
      print(f'Rolling {self.dice_amount} dice...')

      rolled_dice = roller(self.dice_amount)
      formatted_dice = str(rolled_dice).strip('([])').replace(",","")
      print('*** ' + formatted_dice + ' ***')

      if GameLogic.calculate_score(rolled_dice) == 0:
        print('Farkled')
        continue

      print('Enter dice to keep, or (q)uit:')
      response = input('> ')

      if response == 'q':
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        sys.exit()

      else:
        response_list = tuple(map(int, list(response)))
        score = GameLogic.calculate_score(response_list)
        self.banker.shelf(score)
        self.dice_amount -= len(response_list)
        print(f'You have {self.banker.shelved} unbanked points and {self.dice_amount} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')
        response = input('> ')

      if response == 'b':
        self.banker.bank()
        self.dice_amount = 6
        print(f'You banked {score} points in round {self.round_counter}')
        print(f'Total score is {self.banker.balance} points')
      
      elif response == 'r':
        if self.dice_amount == 0:
          self.dice_amount = 6
        continue

      elif response == 'q':
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        sys.exit()

if __name__ == "__main__":
  game = Game()
  game.play()
