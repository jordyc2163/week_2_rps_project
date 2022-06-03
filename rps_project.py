from random import randint
from art import *
rps_option1 = """
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \      /::::\   \:::\    \       \:::\   \:::\    \   
  /::::::\   \:::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\  /\   \:::\   \:::\    \ 
/:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    |/::\   \:::\   \:::\____\\
\::/   |::::\  /:::|____|\::/    \:::\  /:::|____|\:::\   \:::\   \::/    /
 \/____|:::::\/:::/    /  \/_____/\:::\/:::/    /  \:::\   \:::\   \/____/ 
       |:::::::::/    /            \::::::/    /    \:::\   \:::\    \     
       |::|\::::/    /              \::::/    /      \:::\   \:::\____\    
       |::| \::/____/                \::/____/        \:::\  /:::/    /    
       |::|  ~|                       ~~               \:::\/:::/    /     
       |::|   |                                         \::::::/    /      
       \::|   |                                          \::::/    /       
        \:|   |                                           \::/    /        
         \|___|                                            \/____/       

"""

lose_pic = """
  ୧༼ಠ益ಠ༽︻ YOU LOSE!
******************************
"""
win_pic = """
♪┏(°.°)┛┗(°.°)┓┗(°.°)┛┏(°.°)┓ ♪ You WIN!
******************************
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# function to create score border 
def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

while True:
    print(f"""
    {rps_option1}
    {'*'*20} WELCOME TO ROCK PAPER SCISSORS! {'*'*20}
    """)
    # intro
    print(f"Play")
    print(f"Rules")
    print(f"Quit")

    
    menu_input = input("> ").lower() 
    if menu_input == "rules":
        print(bordered(f"""
        {"*" * 10} THE GAME IS ROCK, PAPER, SCISSORS {"*" * 10}
        To win:
        - Simply choose a move, either 'rock', 'paper', or 'scissors'
            - Rock beats Scissors
            - Scissors beat Paper
            - Paper beats Rock
        """))
        
        return_input = input("Would you like to return to the menu? (yes/no) ").lower()
        if return_input == "yes":
            continue
        else:
            break
    if menu_input == "play":
    # play
        player_score = 0
        comp_score = 0
        while True:
            num = randint(1, 3)
            # making the random integer (variable makes it easy to place in code)
            if num == 1:
                comp_move = "rock"
            elif num == 2:
                comp_move = "paper"
            elif num == 3:
                comp_move = "scissors"
            # pre setting the variable comp_move to exist as a readable move 
            # a number is generated before the game even begins

            player_move = input("enter your move ").lower()
            print("YOUR MOVE: ")

            if player_move == "rock":
                print(rock)
            elif player_move == "paper":
                print(paper)
            elif player_move == "scissors":
                print(scissors)
            # user input's move creates the image; no winning condition has been set yet
            print()
            print("COMPUTER MOVE")
            # regardless of the user's decision, it is now the computer's turn so we print the statement

            if comp_move == "rock":
                print(rock)
            elif comp_move == "paper":
                print(paper)
            elif comp_move == "scissors":
                print(scissors)
            # copy and pasted from the above since we want to see what the computer move is. This condition is performed after player's move even though the move was generated before the game started. 


            # we now tell the user if they won or not with the winning conditions
            if player_move == comp_move:
                print("It's a tie!")
            elif player_move == "rock" and comp_move == "scissors" or player_move == "paper" and comp_move == "rock" or player_move == "scissors" and comp_move == "paper":
                print(win_pic)
                player_score += 1
            else:
                print(lose_pic)
                comp_score += 1

            print(bordered(f"Total Wins -- {player_score}"))
            print(bordered(f"Total Losses -- {comp_score}"))
            game_input = input("Would you like to play again? (Type yes/no) ")
            if game_input == "yes":
                continue
            else:
                break
    if menu_input == "quit":
        print("Thanks for playing!")
        break

        



