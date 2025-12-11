# conftest.py
import os
import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

IS_CI = os.getenv("CI") is not None  # True в GitHub Actions и большинстве раннеров


# noinspection PyBroadException
@pytest.fixture(scope="function")
def driver_chrome():
    # Локальная попытка установить chromedriver (безопасно)
    try:
        chromedriver_autoinstaller.install()
    except Exception:
        pass

    options = ChromeOptions()
    if IS_CI:
        # В CI запускаем headless (необязательно, но совместно с xvfb-run)
        options.add_argument("--headless=new")
    # НЕ используем maximize_window() — оно вызывает CDP-команды которые в раннере могут отсутствовать
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")

    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass


# noinspection PyBroadException
@pytest.fixture(scope="function")
def driver_edge():
    options = EdgeOptions()
    if IS_CI:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")

    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass
