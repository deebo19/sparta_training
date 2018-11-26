"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If
you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor
of 26 because 26 / 13 has no remainder.)"""


def get_number():
    num = int(input('Enter any number to find divisors: '))
    return num


def get_divisors():
    new_list = []
    num = get_number()
    x = range(1, num + 1)
    for element in x:
        if num % element == 0:
            new_list.append(element)
    print("The divisors for this number are:" + str(new_list))


get_divisors()
