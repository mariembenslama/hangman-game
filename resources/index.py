from rich import print
from introduction import intro, startHangman, continueGame
from contextChoices import contextChoice
from modeChoices import modeChoice, showVocabulary
from levels import play
from utils import response, disagree
from localization import _, local

local()
intro()

startHangman()

keepPlaying = True
while(keepPlaying):
    vocabulary = contextChoice()
    showVocabulary(vocabulary) if(modeChoice()) else None
    play(vocabulary)
    keepPlaying = continueGame()

exit()