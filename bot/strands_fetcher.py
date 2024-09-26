from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger import logger
import time

# 8x6 grid


def open_grid_board(driver):
    driver.get("https://www.nytimes.com/games/strands")
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "button._momentButton_m3x3m_1._primary_m3x3m_113._default_m3x3m_1",
            )
        )
    )
    start_button.click()

    close_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "xwd__modal--close"))
    )
    close_button.click()


def retrieve_grid(driver):
    board = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "styles-module_board__D_Xt6"))
    )
    char_list = board.text.strip().split("\n")
    grid = [char_list[i : i + 6] for i in range(0, len(char_list), 6)]
    return grid


def fetch_daily_grid():
    driver = webdriver.Chrome()
    logger.info("opening grid board")
    open_grid_board(driver)
    logger.info("retrieving grid")
    logger.info("test")
    grid = retrieve_grid(driver)
    prettyGrid = "\n".join([" ".join(row) for row in grid])
    logger.info(f"successfully retrieved grid:\n{prettyGrid}")
    return grid
