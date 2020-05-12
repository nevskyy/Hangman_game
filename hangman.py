import random
print('H A N G M A N')
option = ''

while True:
    option = input('Type "play" to play the game, "exit" to quit: ').lower().strip()
    if option == 'exit':
        break
    elif option != 'play':
        continue

#def hangman():

    puzzled_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    encoded = list('-' * len(puzzled_word))
    user_attempts = 0
    user_letters = set()
    ascii_lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"

    while user_attempts < 8 and ''.join(encoded) != puzzled_word:
        print()
        print(''.join(encoded))
        user_letter = input('Input a letter: ')
        if user_letter in puzzled_word and user_letter not in user_letters \
                and user_letter in ascii_lowercase_letters and len(user_letter) == 1:
            for i in range(len(puzzled_word)):
                if user_letter == puzzled_word[i]:
                    encoded[i] = user_letter
            user_letters.add(user_letter)
        elif len(user_letter) != 1:
            print("You should print a single letter")
        elif user_letter not in ascii_lowercase_letters:
            print("It is not an ASCII lowercase letter")
        elif user_letter in user_letters:
            print("You already typed this letter")
            user_letters.add(user_letter)
            # user_attempts += 1
        elif user_letter not in puzzled_word and user_letter not in user_letters:
            print("No such letter in the word")
            user_letters.add(user_letter)
            user_attempts +=1
        else:
            print("No such letter in the word")
            user_attempts += 1
    if ''.join(encoded) == puzzled_word:
        print('You guessed the word!\nYou survived!')
    else:
        print('You are hanged!')
    print()


# option = ''
# while option != "play" or option != "exit":
#     option = input('Type "play" to play the game, "exit" to quit: ').lower().strip()
#     if option == "play":
#         hangman()
#     else:
#         break
# initialization = input('Type "play" to play the game, "exit" to quit: > ').lower().strip()
