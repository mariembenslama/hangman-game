from utils import response, agree
from rich import print

def modeChoice(vocabulary):
    mode = input('Easy mode? [Yes/No]: ')
    if(response(mode) and agree(mode)):
        print('this is the vocabulary we will be using for this game:\n', vocabulary)