#=====================================
import selenium.webdriver as webdriver
import time
#=====================================
from seleniumjs import History
from seleniumjs import Console
from seleniumjs import Location
#=====================================

#Initialize Driver
try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Firefox()
finally:
    driver.get('https://github.com/shashankrnr32/SeleniumJS#usage')
    
    location = Location(driver)
    console = Console(driver)
    history = History(driver)
    
    #Test Console and Location Class
    console.log(location.hash)
    time.sleep(5)
    
    console.clear()
    
    console.error('Error Generated Using seleniumjs')
    
    print(location.hash)
    location.href = 'https://www.yahoo.com'
    
    console.clear()
    console.log('seleniumjs working at '+location.hostname)
    
    time.sleep(2)
    
    #Test History Class
    print('Length of History : {}'.format(history.length))
    history.back()
