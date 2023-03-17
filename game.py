from phrase import Phrase
import random

class Game:

    def __init__(self):
        self.phrases = ["Hello world !",
			"How are you ?",
			"I'm John",
			"It's nice to meet you !"
			"What's your favorite color ?"
			]
        self.active_phrase = Phrase(self.phrases[random.randint(0, len(self.phrases) - 1)])
        self.guesses = [' ']
        self.game_continues = True
        self.missed = 0

    def start(self):
        print("Welcome to the Phrase Hunter !!!")
        print("Guess the phrase before you run out of guesses.")
        print("You have a total of 5 guesses to guess the Phrase.")
        print("There is no certain format to follow, you do not have to include punctuation in your guesses.")
        print("However Capitalization is important")

        self.active_phrase.display(self.guesses)

        while self.missed != 5 and self.game_continues:
            self.attempt = input("\nEnter a letter: ")
            if self.active_phrase.check_letter(self.attempt):
                self.guesses.append(self.attempt)
            else:
                self.missed += 1
                print(f"Incorrect! You have {5 - self.missed} out of 5 guesses left.")
            self.active_phrase.display(self.guesses)
            if Phrase.check_complete(self, self.active_phrase.chosenPhrase, self.guesses):
                print("\nYay !!! Congratulations you've won !!!")
                self.game_continues = False
        if self.missed == 5:
            print("\nOh no ! Seems like you've lost !")
