from phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.guesses = [" "]
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        
    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase
        
    def welcome(self):
        print("----------\n  Welcome to Phrase Hunter\n----------")
        
    def get_guess(self):
        return input("\nEnter a letter: ")
        
    def game_over(self):
        if self.missed >= 5:
            print("Oh no ! Seems like you've lost !")
        else:
            print("Yay !!! Congratulations you've won !!!")
