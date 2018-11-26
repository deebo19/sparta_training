'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
that reads the same forwards and backwards.)'''


def get_word():
    word = list(input("please enter your word: "))
    return word


def check_word():
    word = get_word()
    new_word = (word[::-1])
    if word == new_word:
        print("your word is a palindrome")
    else:
        print("your word is not a palindrome")


check_word()