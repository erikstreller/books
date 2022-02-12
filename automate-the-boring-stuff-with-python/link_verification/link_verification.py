# link_verification.py

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.deepl.com/de/translator"


def link_verification():
    # run chrome in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(URL)

    # get all links and set initial counting values
    link_elements = driver.find_elements(By.XPATH, "//a[@href]")
    link_count = 0
    broken_count = 0

    # check for broken links
    for link in link_elements:
        link_href = link.get_attribute("href")
        link_count += 1
        try:
            reqs = requests.get(link_href)
            if reqs.status_code == 404:
                broken_count += 1
                print(f"# Broken link: {link_href}")
            else:
                print(f"Working: {link_href}")
        except:
            continue

    # print stats
    print(f"There were {link_count} links.")
    print(f"And {broken_count} were broken.")


if __name__ == "__main__":
    link_verification()
