#import the random module
import random
#list of swedish berries 
berries = ["hallon", "björnbär", "blåbär", "jordgubbar", "vinbär", "hjortron", "körsbär", "lingon", "havtorn", "enbär", "kråkbär", "olvon", "rönnbär", "nypon", "smultron", "stenbär"]
# print(words)
#variable with the randomly chosen word
chosen = random.choice(berries)
# print(len(chosen))
max_try = len(chosen)
counter = 0
#Displays the number of "_" for the legnth of the chosen word in a new list
display_word = ["_" for i in range(len(chosen))]
print(f"I am thinking about an edible berry that grows in Sweden, it has {len(chosen)} letters")
#create placeholders for chosen word
for i in range(len(chosen)):
    print("_", end=" ")
while counter != max_try:
    guess = str((input("\nGuess one or more letters: \n")))
    #Takes the correct letter and adds to the displayed placeholderss
    if guess == "":
        print("Please enter a letter")
    else:
        if len(guess) == len(chosen) and guess == chosen:
            print("\nWow! That was a great guess!")
            break
        elif guess in chosen:
            print(f"\"{guess}\" is in the word")
            for index, letter in enumerate(chosen):
                if letter == guess:
                    display_word[index] = letter
        else:
            print(f"Sorry, {guess} is not in this word. Try again")
            counter +=1
    if  "_" not in display_word:
        print(f" ".join(display_word),"\nWell done! {chosen} is the correct berry")
        break
    #Print placeholders with correctly guessed letters            
    print(" ".join(display_word))   
    if counter == max_try:
        print(f"Game over! {chosen} was the correct word")
        break