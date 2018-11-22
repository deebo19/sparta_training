# Write a short program that prints each number from 1 to 100 on a new line.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


class FizzBuzz:
    start = 0
    finish = 0

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def print_numbers(self):

        while self.start <= self.finish:
            if self.divisible_by_n(3):
                if self.divisible_by_n(5):
                    print('FizzBuzz')
                else:
                    print('Fizz')
            elif self.divisible_by_n(5):
                print('Buzz')
            else:
                print(self.start)
            self.start += 1

    def divisible_by_n(self, n):
        if self.start % n == 0:
            return True

        return False


x = FizzBuzz(1, 100)
x.print_numbers()



