from Game import Game
import numpy as np
import pandas as pd


class Bonus:
    vowel_set = {"A", "E", "I", "O", "U"}

    def __init__(self, word: str = ""):
        self.game = Game(word, True)
        self.consonantsLeft = 3
        self.vowelsLeft = 1

    def select_letters(self):
        while self.consonantsLeft > 0:
            consonant = input("> Choose a consonant: ").upper()
            if len(consonant) != 1:
                print("Incorrect size.")
                continue
            if consonant in self.game.chosenLetters:
                print("Already selected.")
                continue
            if consonant in Bonus.vowel_set:
                print("Not a consonant.")
                continue
            self.game.fill_letters(consonant)
            self.consonantsLeft -= 1
            print(f"Current Board: {self.game.__str__()}")

        while self.vowelsLeft > 0:
            vowel = input("> Choose a vowel: ").upper()
            if len(vowel) != 1:
                print("Incorrect size.")
                continue
            if vowel in self.game.chosenLetters:
                print("Already selected.")
                continue
            if vowel not in Bonus.vowel_set:
                print("Not a vowel.")
                continue
            self.game.fill_letters(vowel)
            self.vowelsLeft -= 1
            print(f"Current Board: {self.game.__str__()}")

    def make_guess(self, answer):
        return self.game.make_guess(answer)


if __name__ == "__main__":
    inputWord = input("> Choose a word (or RANDOM): ")
    if inputWord == "RANDOM":
        df = pd.read_csv("combined.csv")
        df_sample = df.sample()
        print(f"Category is {df_sample['Category'].iloc[0]}")
        myBonus = Bonus(df_sample['Answer'].iloc[0])
    else:
        myBonus = Bonus(inputWord)
    print(f"Current Board: {myBonus.game.__str__()}")
    myBonus.select_letters()
    solved = False
    while not solved:
        attempt = input("> make a guess (or 'end' to give up): ")
        if attempt == "end":
            print(myBonus.game.word)
            break
        solved = myBonus.make_guess(attempt)
        print(solved)
    print("program ended")
