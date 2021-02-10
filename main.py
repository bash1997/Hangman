import random
import hangman_art
import hangman_words
from replit import clear


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
win = "You win!"
winning = 0
lost = "YOU LOSE!"
losing = 0
guessed = []

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
    if guess in guessed:
        print(f"Sorry, already guessed '{guess}', try again.")
        if guess not in chosen_word:
            lives +=1
    guessed += guess

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry, the letter: {guess} is not in this word. Try again.")
        if lives == 0:
            end_of_game = True
            print(lost)
            losing += 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(win)
        winning += 1


    if lives > 6:
        lives = 6
    print(hangman_art.stages[lives])
    if end_of_game == True:
        again = input("Would you like to play again? Y/N: ").lower()

        if (again == "y") or (again == "yes"):
            chosen_word = random.choice(hangman_words.word_list)
            word_length = len(chosen_word)
            end_of_game = False
            lives = 6
            guessed = []
            display = []
            clear()
            print(hangman_art.logo)
            for _ in range(word_length):
                display += "_"
            print(display)
        print(f"Won: {winning} || Lose: {losing}")
 
