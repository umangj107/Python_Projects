from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "YOUR LOCAL CHROME DRIVER PATH"
SIMILAR_ACCOUNT = "TARGET ACCOUNT USERNAME"
USERNAME = "YOUR INSTAGRAM USERNAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"
INSTA_LOGIN_PATH = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(INSTA_LOGIN_PATH)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/'
                                          'div/div/div/section/div/button').click()

        time.sleep(2)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


    def find_followers(self):
        search_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/'
                                                       'div[2]/div/div/div[2]/input')
        search_box.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)

        searched_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]'
                                                             '/div/div/div[2]/div[3]/div/div[2]/div/div[1]'
                                                             '/a')
        searched_account.click()
        time.sleep(2)

        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/'
                                          'div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)

        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()



instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()
instafollower.follow()
