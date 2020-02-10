from selenium import webdriver
import secrets

# driver_path = '/chromedriver_win32/chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)

# options = webdriver.ChromeOptions()
# options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
# driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Utility/BrowserDrivers/chromedriver.exe")

print(secrets.usuario)
class Bot():
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
        self.driver = driver

        self.driver.get("https://facebook.com")

        log_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')

        user_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')

        user_in.send_keys(secrets.usuario)
        pass_in.send_keys(secrets.password)
        
        log_btn.click()