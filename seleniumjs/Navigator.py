'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_navigator.asp
'''
class Navigator:
    def __init__(self, driver):
        self.driver = driver
        
    @property
    def appCodeName(self):
        return self.driver.execute_script('return navigator.appCodeName')
    
    @property
    def appName(self):
        return self.driver.execute_script('return navigator.appName')
    
    @property
    def appVersion(self):
        return self.driver.execute_script('return navigator.appVersion')
    
    @property
    def cookieEnabled(self):
        return self.driver.execute_script('return navigator.cookieEnabled')
    
    
    @property
    def language(self):
        return self.driver.execute_script('return navigator.language')

    @property
    def onLine(self):
        return self.driver.execute_script('return navigator.onLine')

    @property
    def platform(self):
        return self.driver.execute_script('return navigator.platform')
    
    @property
    def product(self):
        return self.driver.execute_script('return navigator.product')
    
    @property
    def userAgent(self):
        return self.driver.execute_script('return navigator.userAgent')
    
    def javaEnabled(self):
        return self.driver.execute_script('return navigator.javaEnabled()')
     
    