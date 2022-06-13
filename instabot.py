import time
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instabot:
    def __init__(self, driver_path, username, password):
        self.browser = webdriver.Chrome(driver_path)
        self.username = username
        self.password = password

    def accept_cookies(self):
        cookies = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/button[1]')
        cookies.click()
        time.sleep(3)

    def login(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(5)
        self.accept_cookies()
        user_input = self.browser.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        user_input.send_keys(self.username)
        time.sleep(3)
        pwd_input = self.browser.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        pwd_input.send_keys(self.password)
        pwd_input.submit()
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


    def search(self, keyword):
        search = self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys('#{}'.format(keyword))
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        time.sleep(3)

    def like(self, amount):
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
        for i in range(amount):
            time.sleep(randrange(1, 6))
            self.browser.find_element_by_xpath(
                '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(1)
            self.browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()

        self.browser.close()
