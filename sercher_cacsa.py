import asyncio
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Константы
TIMEOUT = 1


async def get_schedule(name):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/usr/bin/google-chrome'
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--log-level=3")

    # chrome_options.proxy = prox

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(2048, 1080)

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, driver.get, 'https://cacs.ws')

    try:
        input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Поиск на Каксе"]')

        input_element.send_keys(name)

        for _ in range(10):
            try:
                elements = driver.find_element(By.XPATH,
                                               f'//a[contains(@class, "Searchbar_searchbar__option__VOoIz")and contains(., "{name}")]')
                break
            except NoSuchElementException as e:
                print('NoSuchElementException')
                await asyncio.sleep(TIMEOUT)

        elements.click()

        await make_screenshot(driver, loop, '1.png')

        elements = driver.find_elements(By.CLASS_NAME,
                                       'Button_button__PjVhE')

        elements[-1].click()

        await asyncio.sleep(TIMEOUT)

        await make_screenshot(driver, loop, '2.png')

    finally:
        driver.quit()


async def make_screenshot(driver, loop, path):
    for _ in range(10):
        try:
            element = driver.find_element(By.CSS_SELECTOR, "main div.wrapper.Timetable_timetable___l88y")
            break
        except NoSuchElementException as e:
            print('NoSuchElementException')
            await asyncio.sleep(TIMEOUT)

    page_width = await loop.run_in_executor(None, driver.execute_script, "return document.body.scrollWidth")
    page_height = await loop.run_in_executor(None, driver.execute_script, "return document.body.scrollHeight")

    driver.set_window_size(width=page_width, height=page_height)

    await loop.run_in_executor(None, driver.save_screenshot,
                               path)

