# Instagram_view-like-bot
Instagram bot to view and like all the photos at once of a user by simply giving his instagram user_id 

modules:

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from time import sleep

from selenium.common.exceptions import NoSuchElementException



functions:
login(username,password): function access the instagram login page and enters your username and password in the requires field and automatically press the enter. It also makes the notification pop up to not now setting

search_user(user_id): it makes the bot to select the search bar and enter the user_id and then select the pofile of the user_id

view_pic() : it makes the bot to open all the pic of the user_id one by one

like_pic() : it likes all the pic of the profile visited
