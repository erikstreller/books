# image_site_downloader.py

import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://unsplash.com/"

# open unsplash.com
# search for images
# download five images


def dl_unsplash_images(search_text: str) -> None:
    # create folder in current working directory
    directory = Path(__file__).parent.resolve()
    folder = Path("unsplash")

    path = directory / folder
    path.mkdir(exist_ok=True)

    # disable logging information
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # open chrome and go to unsplash.com
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get(URL)

    # find input element, input seach_text and submit form
    search_element = driver.find_element(By.NAME, "searchKeyword")
    search_element.send_keys(search_text)
    search_element.submit()

    # wait for image results to be loaded
    try:
        picture_element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//img[@itemprop='thumbnailUrl']")
            )
        )

        # download the first five images
        i = 0
        for image in picture_element[:5]:
            file_path = path / Path(f"{search_text}{i}.png")

            with open(file_path, "wb") as file:
                file.write(image.screenshot_as_png)
            i += 1

        # show the browser two more seconds (not necessary)
        time.sleep(2)
    finally:
        driver.quit()


if __name__ == "__main__":
    search_text = "neon"
    dl_unsplash_images(search_text)
