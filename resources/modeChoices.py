from rich import inspect
from utils import response, agree
from rich import print
from localization import _ 

def modeChoice():
    mode = input(_("easy_mode_yes_no"))
    return True if(response(mode) and agree(mode)) else False

def showVocabulary(vocabulary):
    print(_("this_is_the_vocab_that_we_will_be_using"))
    print(vocabulary)
