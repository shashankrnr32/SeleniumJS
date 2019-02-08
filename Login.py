'''
MIT License
Copyright (c) 2018-2019 Shashank Sharma and IEEE-RIT Web Team

Script by : Shashank Sharma (shashankbsharma@yahoo.com)
Tested on :
    OS : Windows 10, Ubuntu 18.04
    Browser : Google Chrome, Chromium
'''
#=====================================
import selenium.webdriver as webdriver
#=====================================
from seleniumjs.Console import Console
from seleniumjs.Location import Location
import time

driver = webdriver.Firefox()
console = Console(driver)
a = {'e':'bu','suv':'fdsihf'}
console.time()
time.sleep(2)
console.timeEnd()
console.log('hi')

driver.get('https://in.yahoo.com/?p=us#darla-assets-js-top')
location = Location(driver)
print(location.hash)

from seleniumjs.Storage import SessionStorage
sessionStorage = SessionStorage(driver)
sessionStorage.setItem('trial_key','hello_world')

console.log(sessionStorage.getItem('trial_key'))
sessionStorage.clear()
time.sleep(5)
console.clear()


