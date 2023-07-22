# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


opts = webdriver.FirefoxOptions()
opts.add_argument("--headless")
print("Created options")
installation = GeckoDriverManager().install()
print("Installed")
driver = webdriver.Firefox(service=FirefoxService(installation), options=opts)
print("Created the driver")
