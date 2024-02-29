
# What is random class in Python?

# The Python import random module in Python defines a series of functions for generating 
#or manipulating random integers. Python random() is a pseudo-random number generator 
#function that generates a random float number between 0.0 and 1.0, is used by functions 
#in the random module.

import math
import random


def is_win(player, opponent):
  # return true if player wins
  # possible scenarios: r > s, s > p, p > r
  return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

def play_game():
  user=input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
  #changing user choice to lowercase
  user = user.lower()
  #computer choice
  computer = random.choice(['r','p','s'])

  #tie
  if user == computer:
    print("It's a tie, you are the computer have both chosen ", user,"\n")
    return (0, user, computer)
  if is_win(user, computer):
    print("You won, you chose ", user," computer chose ",computer, "\n")
    return (1, user, computer)
  print("You lost, you chose ", user,"the computer chose ",computer)
  return (-1, user, computer)
  

def play_best_of(n):
#initialize two varaible 
  player = 0
  computer_win = 0 
  #play game n times
  wins_needed =math.ceil(n/2)
  print(wins_needed)
  while player < wins_needed and computer_win < wins_needed:
    result, user, computer = play_game()
    if result == 0:
      print("It's a tie, you are the computer have both chosen ", user)
    elif result == 1:
      player += 1
      print("You won you chose ", user,"the computer's choice was.",computer)
    else:
      computer_win += 1
      print("You lost you chose", user,"the computer's choice was.",computer) 
      
  if player > computer_win:
    print("Hurray!!!! You won the best of", n)
  else:
    print("The computer won...:( You lost the best of", n)


def my_function(): 
  print("Hello From My Function!")

  

if __name__=='__main__':
  print("Welcome to Rock, Paper, Scissors")
  How_many = int(input("How many games do you want to play?"))

  for _i in range(How_many):
    print()
    play_game()
  
  

    