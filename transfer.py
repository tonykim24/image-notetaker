from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from notion_client import Client


def transfer():
    url = "https://stackedit.io/app#"
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(3)
    start = driver.find_element(
        "xpath", "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/pre")
    start.clear()
    time.sleep(1)
    file_path = "note.txt"
    with open(file_path, "r") as file:
        text = file.read()
    time.sleep(1)
    start.send_keys(text)

    print("sofar sogood")

# might add more
