from rich import print
from utils import response, disagree
from localization import _

def intro():

    hangmanIntro()
    userIntro()
    continueHangman()
    continueHangmanTuto()

def hangmanIntro():
    print(_('hi_welcome_to_hangman'))


def userIntro():
    name = input(_('whats_your_name'))
    print(_("nice_to_meet_you")+
        " [bold magenta]" + name + "[/bold magenta]! "+
        _("lets_start_the_game"))

def continueHangman():
    confirm = input(_("do_you_want_to_start_the_game_Yes_No"))
    while(not response(confirm)):
        confirm = input(_("do_you_want_to_start_the_game_Yes_No"))

    if(disagree(confirm)):
        print(_("thank_you_lets_play_another_time"))
        exit()

    print(_("alright_lets_do_it"))

def continueHangmanTuto():

    confirm = input("Do you know the rules of the game? [Yes/No]: ")
    while(not response(confirm)):
        confirm = input("Do you know the rules of the game? [Yes/No]: ")

    if(disagree(confirm)):
        hangmanTuto()
    else:
        print("Good! then let's pass to the game")

def hangmanTuto():
    print("Hangman is a sort of guess game, player 1 choose a word of gives alphabets number of the word"+
          ", player 2 tries to guess the alphabets one by one. With each wrong guess, player 1 draws a hanged man"+
          "body parts. When player 2 doesn't guess until the body is drawn completely, he loses! "+
          "Play the game here for quick practice: https://www.gamestolearnenglish.com/hangman/ !")

def startHangman():
    print('\n\n')
    print('Game start!\n\n')

def continueGame():

    confirm = input('Do you want to continue playing? [Yes/No]: ')
    while(not response(confirm)):
        confirm = input('Do you want to continue playing? [Yes/No]: ')

    if(disagree(confirm)):
        print('Thank you for playing, hope to see you again!')
        return False

    return True

