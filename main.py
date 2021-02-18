from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
    

class instalikebot:
    def __init__(self,username,password):
        self.username = username
        self.password =password
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(5)
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.send_keys(self.username)
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sleep(3)
        notification = driver.find_element_by_class_name("HoLwm")
        if notification:
            notification.click()


    def serach_user(self,user_id):
        driver = self.driver
        search = driver.find_element_by_xpath("//input[@placeholder='Search']")
        search.send_keys(user_id)
        sleep(3)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        sleep(4)
       
    def view_pic(self):
        driver = self.driver
        driver.find_element_by_class_name("v1Nh3").click()
        sleep(3)
        while True:
            try:
                next = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
            except NoSuchElementException:
                break
            next.click()
            sleep(3)

        driver.find_element_by_class_name("BI4qX").click()

    def like_pic(self):
        driver = self.driver
        driver.find_element_by_class_name("v1Nh3").click()
        sleep(3)
        while True:
            
            driver.find_element_by_class_name("fr66n").click()
            try:
                next = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
            except NoSuchElementException:
                break
            next.click()
            sleep(3)

        driver.find_element_by_class_name("BI4qX").click()

insta = instalikebot("username","password")
insta.login()
insta.serach_user("user_id")
insta.view_pic()
insta.like_pic()