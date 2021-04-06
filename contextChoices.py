questionRange = 3

switcher = {
    1: "Animals",
    2: "Clothes",
    3: "Food"
}

vocabulary = {
    1: ["bear", "camel", "cat", "kitten", "cow", "crab", "crocodile", "bird", "deer", "dog", "puppy", "dolphin", "duck", "elephant", "fish", 
        "fox", "giraffe", "goat", "hedgehog", "horse", "jellyfish", "kangaroo", "whale", "lion", "monkey", "octopus", "peacock", "pig",
        "rabbit", "seahorse", "shark", "sheep", "shrimp", "snake", "starfish", "tiger", "turtle", "whale", "wolf", "zebra"],
    2: ["belt", "bikini", "blouse", "boots", "boxers", "bra", "cardigan", "cap", "pants", "coat", "dress",
        "dress", "gloves", "hat", "hoodie", "jacket", "jeans", "leggings", "mittens", "pyjamas", 
        "panties", "trousers", "pantyhose", "pullover", "raincoat", "scarf", "shirt", "shoes", "shorts",
        "skirt", "socks", "suit", "sweater", "sweatpants", "sweatshirt", "swimsuit", "tie", "tracksuit", "vest"],
    3: ["apple", "avocado", "banana", "rice", "cake", "candy", "citron", "curry", "egg", "meat", "beef", 
        "tea", "garlic", "chicken", "fish", "seafood", "vegetables", "broccoli", "spinach", "carrots", 
        "onions", "fruit", "sauce", "honey", "hamburger", "cream", "kiwi", "milk", "salad", "yogurt"],
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

        print('Invalid choice, please choose a number between 1 to ' + questionRange + '!')
        contextChoice()

    else:

        return vocabulary.get(int(choice), "Invalid vocabulary choice!")
    