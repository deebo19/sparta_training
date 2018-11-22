"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""
# import getpass


class RockPaper:
    pl_one = None
    pl_two = None
    play_more = None

    def __init__(self):
        pass

    def player_one(self):
        # self.pl_one = getpass.getpass('Player one please enter your choice: ')
        self.pl_one = input('Player one please enter your choice: ')
        return self.pl_one

    def player_two(self):
        # self.pl_two = getpass.getpass('Player two please enter your choice: ')
        self.pl_two = input('Player two please enter your choice: ')
        return self.pl_two

    def play_game(self):
        self.pl_one = self.player_one()
        self.pl_two = self.player_two()
        if self.pl_one == self.pl_two:
            print('It\'s a draw!')
        elif self.pl_one == 'rock' and self.pl_two == 'scissors':
            print("Player one wins")
        elif self.pl_one == 'rock' and self.pl_two == 'paper':
            print("Player two wins!")
        elif self.pl_one == 'paper' and self.pl_two == 'scissors':
            print("Player two wins!")
        elif self.pl_one == 'paper' and self.pl_two == 'rock':
            print("Player one wins!")
        elif self.pl_one == 'scissors' and self.pl_two == 'paper':
            print("Player one wins!")
        elif self.pl_one == 'scissors' and self.pl_two == 'rock':
            print("Player two wins!")
        else:
            print("You didn't enter correctly")
        self.play_again()

    def play_again(self):
        self.play_more = input("Would you like to play again? Yes/No: ")
        while self.play_more == "Yes":
            self.play_game()



x = RockPaper()
x.play_game()