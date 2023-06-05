import secrets

option = ["rock", "paper", "scissors"]

choice_dict = {
    "r":"rock",
    "p":"paper",
    "s":"scissors",
    "e":"exit"
}
table = {
      "games_played": 0,
      "computer": 0,
      "You": 0
    }
fmt_table = ", ".join([f"{key}: {value}" for key, value in table.items()])
print(fmt_table)

# function to show tie and increment number of games played
def tie():
  table["games_played"] += 1
  fmt_table = ", ".join([f"{key}: {value}" for key, value in table.items()])
  print(fmt_table)

# function to increment computer wins and increment number of games played
def comp_win():
  table["games_played"] += 1
  table["computer"] += 1
  fmt_table = ", ".join([f"{key}: {value}" for key, value in table.items()])
  print(fmt_table)

# function to increment computer wins and increment number of games played
def you_win():
  table["games_played"] += 1
  table["You"] += 1
  fmt_table = ", ".join([f"{key}: {value}" for key, value in table.items()])
  print(fmt_table)

while True:
  player_choice = input("\nenter r for rock, p for paper, s for scissors (enter e to exit): ")
  comp_choice = secrets.choice(option)
  player_choice_map = choice_dict.get(player_choice)
  if player_choice_map:    
    if player_choice_map == "exit":
      break
    print(f"\nYour choice is {player_choice_map} and computer choice is {comp_choice}")
    if player_choice_map == comp_choice:
      print("It's a tie, you both chose rock")
      tie()
    elif player_choice_map == "rock":
      if comp_choice == "paper":
        print("Paper cover rock, you lose")          
        comp_win()
      elif comp_choice == "scissors":
        print("Rock smash scissors, you win")
        you_win()
    elif player_choice_map == "paper":
      if comp_choice == "rock":
        print("Paper cover rock, you win")
        you_win()
      elif comp_choice == "scissors":
        print("Scissors cuts paper, you lose")
        comp_win()
    elif player_choice_map == "scissors":
      if comp_choice == "paper":
        print("Scissors cuts paper, you win")
        you_win()
      elif comp_choice == "scissors":
        print("Rock smash scissors, you lose")          
        comp_win()
  else:
    print("Enter a value between 'r', 's', and 'p'.")
print("\nGoodbye...Thanks for playing\n")
