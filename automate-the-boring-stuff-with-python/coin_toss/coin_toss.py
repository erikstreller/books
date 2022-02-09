# coin_toss.py

import random


def guess_coin_toss():
    guess = ""
    coin = ["heads", "tails"]

    print("Two coinflips one guess. Can you guess right?")

    while guess not in (coin):
        guess = input("Enter heads or tails: ")

    toss = random.choice(coin)

    if guess == toss:
        print("#1 You got it first try!")
    else:
        print("#1 Nope first try was a miss! Guess again!")
        toss = random.choice(coin)
        if guess == toss:
            print("#2 You got it second time!")
        else:
            print("#2 Nope. You are really bad at this game.")


if __name__ == "__main__":
    guess_coin_toss()
