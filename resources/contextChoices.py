from vocabularies import vocabulary, switcher, questionRange
from localization import _

def contextChoice():
    
    switcherQuestion = ''

    for choice in switcher:
        switcherQuestion += str(choice) + '. ' + switcher.get(choice, "Invalid switcher choice!") + '\n'
    choice = input(switcherQuestion + _("your_choice"))

    if(not choice.isdigit()):

        print(_("invalid_choice_choose_a_number"))
        return contextChoice()

    elif(int(choice) not in range(1, questionRange + 1)):

        print(_("invalid_choice_please_choose_number_from_1_to_") + "%s !" %questionRange)
        return contextChoice()

    else:
        return vocabulary.get(int(choice), "Invalid vocabulary choice!")
    