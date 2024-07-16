import random


class Game:
    """The Game Itself"""
    wheel_odds = [
        "$100", "$200", "$300", "$500", "Bankrupt", "$1000",
        "$2000", "$3000", "Lose a Turn", "$5000", "$10000",
        "Bankrupt", "$300", "$500", "$1000000",
        "700", "$500", "$300", "$200", "$400",
        "$900", "$600", "Bankrupt", "$700"
    ]

    def __init__(self, word: str = "", rstlne: bool = False):
        assert all(x.isalpha() or x.isspace() for x in word)

        self.balance = 0
        self.chosenLetters = set()
        self.word = word.upper()
        self.guess = []
        for letter in word:
            if letter == " ":
                self.guess.append(" ")
            else:
                self.guess.append("_")
        if rstlne:
            for char in "RSTLNE":
                self.fill_letters(char)

    def fill_letters(self, letter: str) -> int:
        """
        Fills the guess with the letter. Returns number of letters filled
        """
        assert len(letter) == 1
        assert letter.isalpha()

        letter = letter.upper()
        if letter in self.chosenLetters:
            print(f'{letter} was already chosen.')
            return 0

        count = 0
        self.chosenLetters.add(letter)
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.guess[i] = letter
                count += 1
        return count

    def make_guess(self, attempt: str) -> bool:
        """
        Sees if the attempt matches the word
        """
        attempt = attempt.upper()
        if attempt == self.word:
            return True
        return False

    def play(self):
        print("Setting up Game...")
        print("When given the option to perform an action, select 1, 2, or 3")
        print("  1) Spin the wheel")
        print("  2) Buy a vowel")
        print("  3) Make a guess")
        print(self)

        while "_" in self.guess:
            inputNum = input("> What would you like to do (1, 2, or 3): ")
            if inputNum == "1":
                random_outcome = random.choice(Game.wheel_odds)
                if random_outcome == "Bankrupt" or random_outcome == "Lose a Turn":
                    self.balance = 0
                    print("oof")
                    break
                print(f"You landed on {random_outcome}!")
                inputLetter = input("> Choose a letter: ")
                self.balance += self.fill_letters(inputLetter) * int(random_outcome[1:])
                print(f"Current Board: {self.__str__()}, Current Balance: {self.balance}\n")

            elif inputNum == "2":
                inputLetter = input("> Buy a vowel: ")
                self.balance -= 250
                self.fill_letters(inputLetter)
                print(f"Current Board: {self.__str__()}, Current Balance: {self.balance}\n")

            elif inputNum == "3":
                inputAttempt = input("> Make an attempt: ")
                print(self.make_guess(inputAttempt))
                break

            else:
                print("- Incorrect Input. Please try again. -")

    def __str__(self):
        return "".join(self.guess)


if __name__ == "__main__":
    inputWord = input("> Choose a word: ")
    while True:
        input1 = input("> include RSTLNE (Y/N): ").upper()
        if input1 == "Y":
            myGame = Game(inputWord, True)
            break
        elif input1 == "N":
            myGame = Game(inputWord, False)
            break
        print("- Incorrect Input. Please try again. -")
    myGame.play()
    print("Thanks for playing!")
