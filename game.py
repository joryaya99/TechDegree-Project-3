from phrase import Phrase
import random
import os


class Game:

    def __init__(self):
        self.missed = 5
        self.phrases = self.create_phrase()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ',"'",'!',',']


    def create_phrase(self):
        movie_quotes = [
            "May the Force be with you",
            "There's no place like home",
            "I'm the king of the world",
            "I'll be back",
            "There's no crying in baseball",
            "If you build it, he will come",
            "The stuff that dreams are made of",
            "Keep your friends close, but your enemies closer",
            "I am your father",
            "Just keep swimming"
        ]
        phrases = []
        for movie_quote in movie_quotes:
            phrases.append(Phrase(movie_quote))
        return phrases


    def start(self):
        self.welcome()
        while self.missed > 0 and not self.active_phrase.check_complete(self.guesses):
            print("~" * 22)
            print(f' # of tries left : {self.missed}')
            print("~" * 22)
            
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            
            if not user_guess.isalpha():
                print("Letters can only be used, please try again.")
            elif len(user_guess) > 1:
                print("Please enter one letter at a time.")
            elif not self.active_phrase.check_letter(user_guess):
                self.missed -= 1
            os.system("clear")
        self.game_over()

    def get_random_phrase(self):
        return random.choice(self.phrases)


    def welcome(self):
        print("")
        print("=" * 25)
        print(" Guess that Phrase ! ")
        print("=" * 25)
        print("")

    def get_guess(self):
        guess = input("Enter a letter: ")
        return guess.lower()

    def game_over(self):
        if self.missed == 0:
            print("\nOh no ! Seems like you have lost !\n")
        else:
            print(f'\n"{self.active_phrase.phrase}"\n')
            print("Yay !!! Congratulations you have won !!!\n")
