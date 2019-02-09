'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_history.asp
'''
class History:
    def __init__(self,driver):
        self.driver = driver
        
    @property
    def length(self):
        return self.driver.execute_script('return history.length')

    def back(self):
        self.driver.execute_script('window.history.back()')
        
    def forward(self):
        self.driver.execute_script('window.history.forward()')
        
    def go(self,numORurl):
        self.driver.execute_script('window.history.go(arguments[0])',numORurl)