LANGUAGE = ''

english = {
    "hi_welcome_to_hangman": "Hi, welcome to [bold magenta]Hangman[/bold magenta] game!",
    "whats_your_name": "What's your name?",
    "nice_to_meet_you": "Nice to meet you",
    "lets_start_the_game": "Let's start the game!",
    "do_you_want_to_start_the_game_Yes_No": "Do you want to start the game? [Yes/No]: ",
    "thank_you_lets_play_another_time": "Thank you! let's play another time!",
    "alright_lets_do_it": "Alright! let's do it!",
    "do_you_know_the_rules_of_the_game_yes_no": "Do you know the rules of the game? [Yes/No]: "
}

french = {
    "hi_welcome_to_hangman": "Bonjour, bienvenue au jeu [bold magenta]Hangman[/bold magenta]!",
    "whats_your_name": "C'est quoi votre nom?",
    "nice_to_meet_you": "Enchanté de faire votre connaissance",
    "lets_start_the_game": "Commençons le jeu!",
    "do_you_want_to_start_the_game_Yes_No": "Voulez-vous démarrer le jeu? [Yes/No]",
    "thank_you_lets_play_another_time": "Merci! jouons une autre fois!",
    "alright_lets_do_it": "Bien! Faisons le!",
    "do_you_know_the_rules_of_the_game_yes_no": "Connaissez-vous les règles du jeu? [Yes/No]: "
}

def local():
    global LANGUAGE
    LANGUAGE = input('Choose language [English/French]: ')
    while(not start(LANGUAGE)):
        LANGUAGE = input('Incorrect choice\nPlease Choose language [English/French]: ')

def _(s):

    if LANGUAGE.lower().startswith('e'):
        return english[s]
    if LANGUAGE.lower().startswith('f'):
        return french[s]

def start(l):
    return (l.lower().startswith('e') or l.lower().startswith('f') or False)