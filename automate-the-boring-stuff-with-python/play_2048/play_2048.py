# play_2048.py

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as Key
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://play2048.co/"


def play_2048(games_playing: int) -> None:

    # disable logging information
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # open chrome and go to play2048.co
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get(URL)

    # get all the elements and accept cookies
    time.sleep(0.5)
    html_element = driver.find_element(By.CSS_SELECTOR, "html")
    retry_element = driver.find_element(By.CLASS_NAME, "retry-button")
    cookies_element = driver.find_element(By.ID, "ez-accept-all")
    best_element = driver.find_element(By.CLASS_NAME, "best-container")
    score_element = driver.find_element(By.CLASS_NAME, "score-container")

    cookies_element.click()

    # variables for playing and stat tracking
    key_strokes = [Key.UP, Key.RIGHT, Key.DOWN, Key.LEFT]
    games_played = 0
    scores = []

    # play a number of times by pressing the arrow keys
    while games_played != games_playing:

        time.sleep(0.05)
        for key in key_strokes:
            html_element.send_keys(key)

        # append the current score and check for game over
        try:
            scores.append(score_element.text)
            retry_element.click()
            games_played += 1
            continue

        # delete the current score if the game is in progress
        except:
            scores.pop()
            continue

    # print stats
    print(f"You have played: {games_played} games")
    print(f"Your best score was: {best_element.text}")
    print(f"Individual scores were: {scores}")


if __name__ == "__main__":
    games_playing = 3
    play_2048(games_playing)
