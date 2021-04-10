from rich import inspect
from utils import response, agree
from rich import print

def modeChoice():
    mode = input('Easy mode? [Yes/No]: ')
    return True if(response(mode) and agree(mode)) else False

def showVocabulary(vocabulary):
    print('this is the vocabulary we will be using for this game:\n')
    inspect(vocabulary, all = True)
