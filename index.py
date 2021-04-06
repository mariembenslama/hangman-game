from rich import print
from introduction import *
from contextChoices import *
from modeChoices import *
from levels import *
from utils import response, disagree

hangmanIntro()
userIntro()
continueHangman()
continueHangmanTuto()

startHangman()
play = True
while(play):
    vocabulary = contextChoice()
    showVocabulary(vocabulary) if(modeChoice()) else None
    levelOne()
    play = continueGame()

exit()