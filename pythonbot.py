from selenium import webdriver
from secrets import username, password
from selenium.webdriver.common.keys import Keys

import time
import urllib
# driver_path = '/chromedriver_win32/chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)

# options = webdriver.ChromeOptions()
# options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
# driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Utility/BrowserDrivers/chromedriver.exe")

class Bot():
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
        self.driver = driver

    def login(self):
        self.driver.get("https://tinder.com")
        time.sleep(4)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = bot.driver.find_element_by_xpath('//*[@id="email"]')
        pass_in = bot.driver.find_element_by_xpath('//*[@id="pass"]')

        email_in.send_keys(username)
        pass_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        # go back to the base window
        self.driver.switch_to_window(base_window)

        time.sleep(2)
        # pass popups
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()                                
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/button[3]')
        like_btn.click()

    def dislike(self):
        # dislike_ = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        # dislike_btn.click()
                                                           
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/button[1]')
        dislike_btn.click()
        
        # self.driver.find_element_by_css_selector('body').send_keys(Keys.LEFT)
        

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def save_screenshot(self, name):
        path = "./screenshots/"
        print("saving image:", name)
        self.driver.save_screenshot(path+name)

    def swipe_reject(self, num_swipes, start_index=1):
        for i in range(num_swipes):
            print(i)
            time.sleep(0.3)
            self.driver.find_element_by_css_selector('body').send_keys(Keys.UP)
            # save the screenshot
            name = "screenshot_{}.png".format(i+start_index)
            self.save_screenshot(name)
            try:
                self.dislike()
            except:
                self.close_popup()

bot = Bot()
bot.login()

'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div/div'
driver.find_element_by_css_selector('body').send_keys(Keys.LEFT)
