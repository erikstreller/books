# comma_code.py

def single_string(list: list[str]) -> str:
    length = len(list)

    if length == 0:
        return "The list was empty."
    elif length == 1:
        return list[0]
    else:
        cutString = ", ".join(list[:-1])
        finalString = f"{cutString} and {list[-1]}"
        return finalString


if __name__ == "__main__":

    spam = ["apples", "tofu", "bananas", "cats", "dogs"]

    print(single_string(spam))
