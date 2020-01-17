from random import randint
import time

def rockpapersci(bot_choice,player_choice):                         #Adds corresponding scores to bot/player
    print("Bot picks : ",bot_choice,"\n")
    selection = player_choice,bot_choice
    if selection in win_list:
        score['player']+=1                                          #Adds a point to the player
    elif player_choice == bot_choice:
        score['ties']+=1                                            #Adds 1 to the number of ties
    else:
        score['bot']+=1                                             #Adds a point to the bot

def winner(bot_score, player_score):                                #Determines the Winner
    if bot_score>player_score:
        print("Bot wins the game ! :(")
    elif bot_score == player_score:
        print("Scores are Tied !")
    else:
        print("You win ! :)")

def discription():                                                               #Discription about the Game
    print("CLASSIC ROCK-PAPER-SCISSORS GAME !")
    option_help = ("\n This game is simple and goes as following:"  
          "\n *You can choose between: Rock, Paper or Scissors."
          "\n\n You must take in consideration that:"
          "\n *Rock crushers Scissors."
          "\n *Scissors cut Paper."
          "\n *Paper covers Rock."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'."
          "\n        *If you want to exit because you're afraid of loosing, just type 'exit' you coward!\n")
    print(option_help)

def play():
    for i in range(5):
        global turn
        turn += 1                                                                   #Number of turns
        print("\n**********   Turn ", turn, "   **********\n")
        bot_choice = randint(0,2)                                                   #bots random choice as index
        player_choice = input("rock/paper/scissors? : ")                            #player's choice
        if player_choice in choice:
            rockpapersci(choice[bot_choice], player_choice.lower())                 
        else:
            print("You have enterd the wrong choice...")
        time.sleep(1)
        print("BOT score : ",score['bot'])
        print("Your score : ",score['player'])
        print("TIES : ",score['ties'])
    winner(score['bot'], score['player'])                                           #Calls winner function

if __name__ == '__main__':
    choice = ["rock", "paper", "scissors"]                                          #Game possibilities
    win_list = [("rock","scissors"),("paper","rock"),("scissors","paper")]          #Winning combinations
    print("Welcome to the CLASSIC ROCK-PAPER-SCISSORS game !\n")
    while(1):
        turn = 0
        score = {'bot':0, 'player':0, 'ties':0}                                     #Score dictionary
        option = int(input("1. READ Discription !\n2. PLAY !\n3. EXIT !\n\n"))
        if option == 1:
            discription()
        elif option == 2:
            play()
        elif option == 3:
            print("Thanks for playing the Game...!!!\n")
            exit(0)
        else:
            print("Enter the right choice...\n")