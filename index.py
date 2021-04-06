from rich import print
from introduction import *
from contextChoices import *
from modeChoices import *

hangmanIntro()
userIntro()
continueHangman()
continueHangmanTuto()

print('\n\n')
print('Game start!\n\n')
vocabulary = contextChoice()
modeChoice(vocabulary)