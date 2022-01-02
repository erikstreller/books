# collatz_sequence.py

def valid_input() -> int:
    try:
        number = int(input("Your number: "))
        return number

    except ValueError:
        print("This is not a number.")
        return valid_input()


def collatz_sequence(number: int) -> int:
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def run_sequence(number) -> None:
    while number != 1:
        number = collatz_sequence(number)
        print(number)


if __name__ == "__main__":

    print("Hello. ", end="")
    number = valid_input()
    run_sequence(number)
