from rich import print
from introduction import *
from contextChoices import *
from utils import response, agree

hangmanIntro()
userIntro()
continueHangman()
continueHangmanTuto()

print('\n\n')
print('Game start!\n\n')
vocabulary = contextChoice()

mode = input('Easy mode? [Yes/No]: ')
if(response(mode) and agree(mode)):
    print('this is the vocabulary we will be using for this game:\n', vocabulary)