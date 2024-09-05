import random

name = input("Nama lu siapa cok? ")
print("oalah kirain sape aja",name, "toh")

kata = ['pelangi', 'komputer', 'sains', 'pemrograman', 'python', 'matematika', 'pemain', 'kondisi', 'sebaliknya', 'air', 'papan', 'capung']
word = random.choice(kata)

print("Tebak Kata nya bosskuh")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    # Loop through each character in the word
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    print()  # To move to the next line after printing the word or dashes

    # If no characters were missing, the user wins
    if failed == 0:
        print("lu menang cok")
        print("ini kata kata nya cok:", word)
        break

    # Ask the user to guess a character
    guess = input("tebak karakter cok: ")
    guesses += guess

    # If the guessed character is not in the word, reduce the number of turns
    if guess not in word:
        turns -= 1
        print("salah bjir")
        print("lu ada", turns, "tebakan lagi")

        if turns == 0:
            print("Lu KALAH WKWKWK COCOTE")
