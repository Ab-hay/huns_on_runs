import time
import random
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Using Selenium to click on the farm list and start reload it.
master_site = "https://ts31.x3.international.travian.com/dorf1.php"
farm_list_url = "https://ts31.x3.international.travian.com/build.php?id=39&gid=16&tt=99"
USERNAME = ''
PASSWORD = ''

# Setup Firefox options (optional)
firefox_options = Options()
firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


# Path to GeckoDriver executable
GECKODRIVER_PATH = "../bin/geckodriver"



def farm(url):
    # Initialize GeckoDriver
    service = Service(GECKODRIVER_PATH)
    browser = webdriver.Firefox(service=service, options=firefox_options)
    browser.get(url)

    # Locate and fill username and password fields
    username = browser.find_element(By.NAME, "name")
    password = browser.find_element(By.NAME, "password")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    # Wait until the button is visible and clickable
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'textButtonV2'))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='name' and text()='Farmlist']"))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'startAllFarmLists'))
    ).click()

    time.sleep(5)

    browser.quit()
    return

def run_farm_list_with_jitter():
    count = 1
    while True:
        print(f"{Fore.YELLOW}Starting farm list, triggered count: {count}{Style.RESET_ALL}")
        try:
            farm(master_site)  # Ensure the 'farm' and 'master_site' are defined in your script
            random_wait_time = random.uniform(290, 480)
            print(f"{Fore.GREEN}waiting for {random_wait_time} before restarting{Style.RESET_ALL}")
            time.sleep(random_wait_time)
            count += 1
        except Exception as ex:
            print(f"{Fore.RED}Error: {ex}{Style.RESET_ALL}")

if __name__ == "__main__":
    run_farm_list_with_jitter()
