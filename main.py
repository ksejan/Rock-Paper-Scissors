import random

def get_choices():
  player_choice = input("Enter a choice (Rock, Paper, Scissors): ")
  
  options = ["Rock","Paper", "Scissors"]
  computer_choice = random.choice(options)
  
  choices = {"player" : player_choice, "computer" : computer_choice}
  return choices

def check_win(player, computer):
  print(f"You choose {player} and the computer choose {computer}")
  if player == computer:
    return "It's a Tie!"
  elif player == "Rock":
    if computer == "Scissors":
      return "Rock smashes Scissors! You win!"
    else:
      return "Paper covers rock. You loose."
  
  