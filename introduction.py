from rich import print
from utils import response, disagree

def hangmanIntro():
    print('Hi, welcome to [bold magenta]Hangman[/bold magenta] game!')

def hangmanTuto():
    print("Hangman is a sort of guess game, player 1 choose a word of gives alphabets number of the word"+
          ", player 2 tries to guess the alphabets one by one. With each wrong guess, player 1 draws a hanged man"+
          "body parts. When player 2 doesn't guess until the body is drawn completely, he loses! "+
          "Play the game here for quick practice: https://www.gamestolearnenglish.com/hangman/ !")

def userIntro():
    name = input("What's your name? ")
    print("Nice to meet you [bold magenta]" + name + "[/bold magenta]!, let's start the game!")

def continueHangman():

    confirm = input('Do you want to start the game? [Yes/No]: ')
    while(not response(confirm)):
        confirm = input('Do you want to start the game? [Yes/No]: ')

    if(disagree(confirm)):
        print("Thank you! let's play another time!")
        exit()

    print("Alright! let's do it!")

def continueHangmanTuto():

    confirm = input("Do you know the rules of the game? [Yes/No]: ")
    while(not response(confirm)):
        confirm = input("Do you know the rules of the game? [Yes/No]: ")

    if(disagree(confirm)):
        hangmanTuto()
    else:
        print("Good! then let's pass to the game")

def startHangman():
    print('\n\n')
    print('Game start!\n\n')