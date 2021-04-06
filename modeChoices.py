from utils import response, agree
from rich import print

def modeChoice():
    mode = input('Easy mode? [Yes/No]: ')
    if(response(mode) and agree(mode)):
        return True 
    else:
        return False

def showVocabulary(vocabulary):
    print('this is the vocabulary we will be using for this game:\n', vocabulary)