# Write a short program that prints each number from 1 to 100 on a new line.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


def print_numbers():
    num = 1
    while num <= 100:
        if num % 3 == 0:
            if num % 5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
        num = num + 1


print_numbers()


