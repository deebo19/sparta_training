"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous
 message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the
ENTER button)"""


def get_details():
    user_name = input("Please enter your name: ")
    print("your name is " + user_name)
    user_age = input("Please enter your age: ")
    user_age = int(user_age)
    print('your age is ' + str(user_age))
    return user_name, user_age


def hundred_years():
    name, age = get_details()

    year_100 = 100 - int(age) + 2018
    print(name + " will turn 100 years old in the year " + str(year_100))


hundred_years()
