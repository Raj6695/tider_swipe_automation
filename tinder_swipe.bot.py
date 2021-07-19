from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

WEB_DRIVER_PATH = "C:\Develop\chromedriver.exe"

EMAIL = "rassss932@gmail.com"
PASSWORD = "Litmus10."
is_on = True


class Tinder_swipe_bot:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        get_page = self.driver.get("https://tinder.com/")
        time.sleep(5)
        login = self.driver.find_element_by_xpath(
            '//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login.click()

    def login_with_fb(self):
        time.sleep(4)
        fb_login_link = self.driver.find_element_by_xpath(
            '//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        time.sleep(3)
        fb_login_link.click()
        time.sleep(2)
        fb_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_window)
        fb_login_page = self.driver.find_element_by_class_name("_55r1 ")
        fb_login_page.send_keys(EMAIL)
        f_password = self.driver.find_element_by_id("pass")
        f_password.send_keys(PASSWORD)
        confirm = self.driver.find_element_by_class_name("uiButtonConfirm ")
        confirm.click()
        time.sleep(7)

    def dismiss_all_requests(self):
        tinder_window = self.driver.window_handles[0]
        self.driver.switch_to.window(tinder_window)
        location_allow = self.driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]')
        location_allow.click()
        match_notify = self.driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[2]')
        match_notify.click()
        time.sleep(7)
        dismiss_likes_view = self.driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div[3]/button[2]')
        dismiss_likes_view.click()

    def hit_like(self):
        time.sleep(5)
        for n in range(100):
            try:
                time.sleep(1)
                swipe = self.driver.find_element_by_xpath(
                    '//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
                swipe.click()
            except NoSuchElementException:
                try:
                    time.sleep(1)
                    swipe = self.driver.find_element_by_xpath(
                        '//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
                    swipe.click()
                except ElementClickInterceptedException:
                    tinder_to_homescreen= self.driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[2]/button[2]')
                    tinder_to_homescreen.click()


bot = Tinder_swipe_bot(WEB_DRIVER_PATH)
bot.login()
bot.login_with_fb()
bot.dismiss_all_requests()
bot.hit_like()
