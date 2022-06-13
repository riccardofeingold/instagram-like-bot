from instabot import Instabot

username = ''
password = ''
filepath_to_chromedriver = ''

bot = Instabot(filepath_to_chromedriver, username, password)
bot.login()
bot.search('entrepreneurship')
bot.like(10)
