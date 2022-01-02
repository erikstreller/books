# regex_strip.py

import re


def regex_strip(text: str, arg: str) -> str:
    if arg:
        trim = f"[{re.escape(arg)}]*"
    else:
        trim = r"\s*"

    return re.fullmatch(f"{trim}(.*?){trim}", text).group(1)  # type: ignore


if __name__ == "__main__":

    text = "+ -   to much things * 3   .*"
    strip = ".+- *"

    print(f"<{regex_strip(text, strip)}>")
