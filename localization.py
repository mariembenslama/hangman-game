LANGUAGE = ''

english = {
    "hi_welcome_to_hangman": "Hi, welcome to [bold magenta]Hangman[/bold magenta] game!",
    "whats_your_name": "What's your name?",
    "nice_to_meet_you": "Nice to meet you, ",
    "lets_start_the_game": " Let's start the game!",
    "do_you_want_to_start_the_game_Yes_No": "Do you want to start the game? [Yes/No]: ",
    "thank_you_lets_play_another_time": "Thank you! let's play another time!",
    "alright_lets_do_it": "Alright! let's do it!",
    "do_you_know_the_rules_of_the_game_yes_no": "Do you know the rules of the game? [Yes/No]: ",
    "good_lets_start_the_game": "Good! then let's pass to the game",
    "hangman_tuto": "Hangman is a sort of guess game, player 1 choose a word and gives alphabets number of the word"+
        ", player 2 tries to guess the alphabets one by one. With each wrong guess, player 1 draws a hanged man"+
        "body parts. When player 2 doesn't guess until the body is drawn completely, he loses! "+
        "Play the game here for quick practice: https://www.gamestolearnenglish.com/hangman/ !",
    "game_start": "\n\nGame start!\n\n",
    "do_you_want_to_continue_playing": "Do you want to continue playing? [Yes/No]: ",
    "thank_you_for_playing_see_you_again": "Thank you for playing, hope to see you again!",
    "your_choice": "\nYour choice: ",
    "invalid_choice_choose_a_number": "Invalid choice, please choose a number!",
    "invalid_choice_please_choose_number_from_1_to_": "Invalid choice, please choose a number between 1 to",
    "easy_mode_yes_no": "Easy mode? [Yes/No]:",
    "this_is_the_vocab_that_we_will_be_using": "This is the vocabulary we will be using for this game:\n",
    "your_guess": "Your Guess: ",
    "sorry_you_lose": "Sorry! this is your lose and our win! Your can try again if you want!\n",
    "you_win": "You won! congrats! the right guess was: \n",
    "stick_drawn": "a stick is drawn!",
    "rope_drawn": "a rope is drawn!",
    "head_drawn": "a head is drawn!",
    "neck_drawn": "a neck is drawn!",
    "shoulder_drawn": "a shoulder is drawn!",
    "right_hand_drawn": "a right hand is drawn!",
    "left_hand_drawn": "a left hand is drawn!",
    "body_drawn": "a body is drawn!",
    "right_foot_drawn": "a right foot is drawn!",
    "left_foot_drawn": "a left foot is drawn!",
}

french = {
    "hi_welcome_to_hangman": "Bonjour, bienvenue au jeu [bold magenta]Hangman[/bold magenta]!",
    "whats_your_name": "C'est quoi votre nom?",
    "nice_to_meet_you": "Enchanté de faire votre connaissance, ",
    "lets_start_the_game": " Commençons le jeu!",
    "do_you_want_to_start_the_game_Yes_No": "Voulez-vous démarrer le jeu? [Yes/No]",
    "thank_you_lets_play_another_time": "Merci! jouons une autre fois!",
    "alright_lets_do_it": "Bien! Faisons le!",
    "do_you_know_the_rules_of_the_game_yes_no": "Connaissez-vous les règles du jeu? [Yes/No]: ",
    "good_lets_start_the_game": "Bien! alors passons au jeu",
    "hangman_tuto": "Le pendu est une sorte de jeu de devinettes, le joueur 1 choisit un mot et donne le nombre des alphabets du mot "+
         ", le joueur 2 essaie de deviner les alphabets un par un. A chaque mauvaise estimation, le joueur 1 dessine une partie du corps du pendu" +
         ". Quand le joueur 2 ne devine pas tant que le corps est complètement dessiné, il perd!" +
         "Jouez au jeu ici pour une pratique rapide: https://www.gamestolearnenglish.com/hangman/!",
    "game_start": "\n\nCommençons le jeu!\n\n",
    "do_you_want_to_continue_playing": "Voulez-vous continuer à jouer? [Yes/No]: ",
    "thank_you_for_playing_see_you_again": "Merci d'avoir joué, j'espère vous revoir!",
    "your_choice": "\nVotre choix: ",
    "invalid_choice_choose_a_number": "Choix invalide, veuillez choisir un numéro!",
    "invalid_choice_please_choose_number_from_1_to_": "Choix invalide, veuillez choisir un nombre entre 1 et",
    "easy_mode_yes_no": "Niveau simple? [Yes/No]:",
    "this_is_the_vocab_that_we_will_be_using": "This is the vocabulary we will be using for this game:\n",
    "your_guess": "Votre estimation: ",
    "sorry_you_lose": "Désolé! c'est votre perte et notre victoire! Vous pouvez réessayer si vous le souhaitez! \n",
    "you_win": "Vous avez gagné! félicitations! la bonne estimation était: \n",
    "stick_drawn": "un bâton est dessiné!",
    "rope_drawn": "une corde est dessiné!",
    "head_drawn": "une tête est dessinée!",
    "neck_drawn": "un cou est dessiné!",
    "shoulder_drawn": "une épaule est dessinée!",
    "right_hand_drawn": "une main droite est dessinée!",
    "left_hand_drawn": "une main gauche est dessinée!",
    "body_drawn": "un corps est dessiné!",
    "right_foot_drawn": "un pied droit est dessiné!",
    "left_foot_drawn": "un pied gauche est dessiné!",
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