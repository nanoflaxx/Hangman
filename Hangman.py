#import the random module
import random
#list of swedish berries 
berries = ["hallon", "björnbär", "blåbär", "jodgubbar", "vinbär", "hjortron", "körsbär", "lingon", "havtorn", "enbär", "kråkbär", "olvon", "rönnbär", "nypon", "smultron", "stenbär"]
# print(words)
#variable with the randomly chosen word
chosen = random.choice(berries)
# print(len(chosen))
max_try = len(chosen)+3
counter = 0
#Displays the number of "_" for the legnth of the chosen word in a new list
display_word = ["_" for i in range(len(chosen))]
print(f"I am thinking about an edible berry that grows in Sweden, it has {range(len(chosen))} letters")
while counter != max_try:
    #create placeholders for chosen word
    for i in range(len(chosen)):
        print("_", end=" ")
    guess = str((input("\nGuess a letter: \n")))
    counter +=1
    #Takes the correct letter and adds to the displayed placeholderss
    if guess in chosen:
        print(f"\"{guess}\" is in the word")
        for index, letter in enumerate(chosen):
            if letter == guess:
                display_word[index] = letter
    elif guess != chosen:
        print(f"Sorry, {guess} is not in this word. Try again")



    #Print placeholders with correctly guessed letters            
    print(" ".join(display_word))   
if counter == max_try:
    print(f"Game over! {chosen} was the correct word")
