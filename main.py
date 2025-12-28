import random


def get_user_guess() -> int:
    """
    Asks the user for a guess and returns it as an integer.
    :return: the user's guess as an integer
    """
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            return guess
        except ValueError:
            print("Please enter a valid number")


def check_guess(secret: int, guess: int) -> bool:
    """ Checks the user's guess against the secret number and provides.
    .number and provides feedbac
    :param secret: the secret number to guess
    :param guess: the user's guess
    :return: True if the guess is correct, False otherwise.
    """
    if guess < secret:
        print("higher!")
        return False
    elif guess > secret:
        print("lower!")
        return False
    else:
        print("exactly right! You win!")
        return True


def play_game() -> None:
    """
    Starts the guessing game.
    :return: None
    """
    secret_number: int = random.randint(1, 100)
    guessed_correctly: bool = False

    print("welcome to the guessing game!")
    while not guessed_correctly:
        user_guess: int = get_user_guess()
        guessed_correctly = check_guess(secret_number, user_guess)


if __name__ == "__main__":
    play_game()
