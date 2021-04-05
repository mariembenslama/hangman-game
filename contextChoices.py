questionRange = 8

switcher = {
    1: "Animals",
    2: "Home",
    3: "Clothes",
    4: "Food",
    5: "Body",
    6: "Jobs",
    7: "Sports",
    8: "Colors",
}

vocabulary = {
    1: ["bear", "camel", "cat", "kitten", "cow", "crab", "crocodile", "bird", "deer", "dog", "puppy", "dolphin", "duck", "elephant", "fish", 
        "fox", "giraffe", "goat", "hedgehog", "horse", "jellyfish", "kangaroo", "whale", "lion", "monkey", "octopus", "peacock", "pig",
        "rabbit", "seahorse", "shark", "sheep", "shrimp", "snake", "starfish", "tiger", "turtle", "whale", "wolf", "zebra"]
    2: [''],
    3: ["belt", "bikini", "blouse", "boots", "boxers", "bra", "cardigan", "cap", "pants", "coat", "dress",
        "dress", "gloves", "hat", "hoodie", "jacket", "jeans", "leggings", "mittens", "pyjamas", 
        "panties", "trousers", "pantyhose", "pullover", "raincoat", "scarf", "shirt", "shoes", "shorts",
        "skirt", "socks", "suit", "sweater", "sweatpants", "sweatshirt", "swimsuit", "tie", "tracksuit", "vest"],
    4: [''],
    5: [''],
    6: [''],
    7: ['twww'],
    8: ['tweet']
}

def contextChoice():
    
    switcherQuestion = ''

    for choice in switcher:
        switcherQuestion += str(choice) + '. ' + switcher.get(choice, "Invalid switcher choice!") + '\n'
    choice = input(switcherQuestion + '\nYour choice: ')

    if(not choice.isdigit()):

        print('Invalid choice, please choose a number!')
        contextChoice()

    elif(int(choice) not in range(1, questionRange + 1)):

        print('Invalid choice, please choose a number between 1 to 8!')
        contextChoice()

    else:

        return vocabulary.get(int(choice), "Invalid vocabulary choice!")
    