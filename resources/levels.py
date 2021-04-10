import random
from localization import _

bodyParts = 10

hangmanBody = {
    1: "stick_drawn",
    2: "rope_drawn",
    3: "head_drawn",
    4: "neck_drawn",
    5: "shoulder_drawn",
    6: "right_hand_drawn",
    7: "left_hand_drawn",
    8: "body_drawn",
    9: "right_foot_drawn",
    10: "left_foot_drawn",
}

def play(vocabulary):

    score = 0
    loss = 0
    guess = ''
    inputWord = ''

    word = random.choice(vocabulary).lower()

    inputWord = initInputWord(word, inputWord)

    while(loss < bodyParts and score < len(word)):
        guess = input(_("your_guess"))
        if(correct(guess, word)):
            score += 1
            inputWord = display(word, word.find(guess.lower()), inputWord)
        else:
            loss += 1
            drawHangman(loss)

    if(loss == bodyParts):
        print(_("sorry_you_lose"))
    else:
        print(_("you_win"), word.upper())
        


def display(word, position, inputWord):
    for value in word:
        if(word.find(value) == position):
            inputWord = inputWord[:position] + value + inputWord[position + 1:]
    
    print(inputWord + ' (' + str(len(word)) + ')')
    return inputWord

def correct(guess, word):
    return word.find(guess.lower()) > -1

def initInputWord(word, inputWord):
    for value in word:
        inputWord += '_'
    print(inputWord + ' (' + str(len(word)) + ')')
    return inputWord

def drawHangman(loss):
    print(_(hangmanBody.get(loss, 'Incorrect body part index')))
