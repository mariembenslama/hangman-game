from rich import print
from introduction import *
from contextChoices import *
from modeChoices import *

hangmanIntro()
userIntro()
continueHangman()
continueHangmanTuto()

startHangman()
vocabulary = contextChoice()
showVocabulary(vocabulary) if(modeChoice()) else None