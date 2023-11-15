# first create a list(menu)

# while to decide user to type of number,if type 5 
# game ended.

def main():   
    game_menu = [
    "\n1.guess color word"
    "\n2.adventure game"
    "\n3.anlancy a File"
    "\n4.other"
    "\n5.quit"
]
    number = None
    while number != 5:
        for k in game_menu:
            print(k)
        number=input('Please enter an action: ')
        # begin the first game of menu.
        if number == "1":
            print("welcome to the guess color word game!")
            # guess = -1
            # # this is a secret word.
            # word = "color"
            number1 = get_number1()
            print(number1)
            # print("Your hint is: ",end="_")
            # for i in word:
            #     print("_",end=" ")
            
            # hint= " " # if the position differ, have a different?
            # print()
            # guess_word = input("Please enter a word: ")
            # # while to decide the guess word is not the defind word.
            # while guess_word != word:
            #     guess_word = input("Please enter a word: ")
                # get the number 1 function
def get_number1():
        guess_count = 0
            # this is a secret word.
        word = "color"
        hint= " "   
        # print("Your hint is: ",end="_")
        guess_word = input("Please enter a word: ")
        print("Your hint is:")
        for i in word:
            print("_",end=" ")
        print()
            # while to decide the guess word is not the defind word.
        while guess_word != word:
            # guess_word = input("Please enter a word: ")
            if len(guess_word) == len(word):
                for i in range(len(word)):
                    if guess_word[i] == word[i]:
                           print(guess_word[i].upper(), end=' ')
                    elif guess_word[i] in word:
                         print(guess_word[i].lower(), end=' ')
                    else:
                         print('_', end=' ')
                if guess_word == word:
                    print('congratulation.')
            else:
                print('sorry.')  
            guess_count += 1
        print(f"it took you {guess_count} guesses")                
        return guess_word
main()
def guess_color_word():
    """
    A game where the user has to guess a color word.
    """
    print("Welcome to the Guess Color Word game!")
    word = "color"
    guess_count = 0
    while True:
        guess = input("Please enter a word: ")
        if guess == word:
            guess_count += 1
            print(f"Congratulations! It took you {guess_count} guesses.")
            break
        else:
            guess_count += 1
            print("Sorry, that's not the correct word.")


