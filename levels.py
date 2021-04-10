import random

bodyParts = 10

hangmanBody = {
    1: 'a stick is drawn!',
    2: 'a rope is drawn!',
    3: 'a head is drawn!',
    4: 'a neck is drawn!',
    5: 'a shoulder is drawn!',
    6: 'a right hand is drawn!',
    7: 'a left hand is drawn!',
    8: 'a body is drawn!',
    9: 'a right foot is drawn!',
    10: 'a left foot is drawn!'
}

def play(vocabulary):

    score = 0
    loss = 0
    guess = ''
    inputWord = ''

    word = random.choice(vocabulary).lower()

    inputWord = initInputWord(word, inputWord)

    while(loss < bodyParts and score < len(word)):
        guess = input('Your Guess: ')
        if(correct(guess, word)):
            score += 1
            inputWord = display(word, word.find(guess.lower()), inputWord)
        else:
            loss += 1
            drawHangman(loss)

    if(loss == bodyParts):
        print('Sorry! this is your lose and our win! Your can try again if you want!\n')
    else:
        print('You won!, congrats! the right guess was: \n', word.upper())
        


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

def finishHangman(word, score):
    return score == len(word)

def drawHangman(loss):
    print(hangmanBody.get(loss, 'Incorrect body part index'))