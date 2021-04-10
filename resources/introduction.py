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

    confirm = input(_("do_you_know_the_rules_of_the_game_yes_no"))
    while(not response(confirm)):
        confirm = input(_("do_you_know_the_rules_of_the_game_yes_no"))

    if(disagree(confirm)):
        hangmanTuto()
    else:
        print(_("good_lets_start_the_game"))
 
def hangmanTuto():
    print(_("hangman_tuto"))

def startHangman():
    print(_("game_start"))

def continueGame():

    confirm = input(_("do_you_want_to_continue_playing"))
    while(not response(confirm)):
        confirm = input(_("do_you_want_to_continue_playing"))

    if(disagree(confirm)):
        print(_("thank_you_for_playing_see_you_again"))
        return False

    return True

