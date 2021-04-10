from vocabularies import vocabulary, switcher, questionRange

def contextChoice():
    
    switcherQuestion = ''

    for choice in switcher:
        switcherQuestion += str(choice) + '. ' + switcher.get(choice, "Invalid switcher choice!") + '\n'
    choice = input(switcherQuestion + '\nYour choice: ')

    if(not choice.isdigit()):

        print('Invalid choice, please choose a number!')
        return contextChoice()

    elif(int(choice) not in range(1, questionRange + 1)):

        print('Invalid choice, please choose a number between 1 to %s !' %questionRange)
        return contextChoice()

    else:
        return vocabulary.get(int(choice), "Invalid vocabulary choice!")
    