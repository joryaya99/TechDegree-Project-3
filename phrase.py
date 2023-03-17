class Phrase():
    def __init__(self, phrase):
        self.chosenPhrase = phrase

    def display(self, attempts):
        for letter in self.chosenPhrase:
            print(f'{letter}', end=' ') if letter in attempts else print('_', end=' ')
    
    def check_letter(self, attempt):
        return attempt in self.chosenPhrase

    def check_complete(self, chosenPhrase, attempts):
        return set(chosenPhrase) == set(attempts)
