'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_storage.asp
'''
class LocalStorage:
    def __init__(self,driver):
        self.driver = driver

    @property
    def length(self):
        return self.driver.execute_script('return localStorage.length')
    
    def xScript(self, method = 'key', argument_index = 0):
        if method == 'setItem':
            return '{0}.{1}(arguments[{2}], arguments[{3}])'.format('localStorage', method, argument_index, argument_index+1)
        return '{0}.{1}(arguments[{2}])'.format('localStorage', method, argument_index)
    
    def key(self, index):
        index = int(index)
        return self.driver.execute_script(
                'return '+self.xScript(method = 'key'), 
                index
                )
        
    def getItem(self, keyname):
        return self.driver.execute_script(
                'return '+self.xScript(method = 'getItem'), 
                keyname
                )
        
    def setItem(self, keyname, value):
        self.driver.execute_script(
                self.xScript(method = 'setItem'), 
                keyname, 
                value
                )
    
    def removeItem(self, keyname):
        self.driver.execute_script(
                self.xScript(method = 'removeItem'),
                keyname
                )

    def clear(self):
        self.driver.execute(
                self.xScript(method = 'clear'),
                None
                )
        
class SessionStorage:
    def __init__(self,driver):
        self.driver = driver
        
    @property
    def length(self):
        return self.driver.execute_script('return sessionStorage.length')
    
    def xScript(self, method = 'key', argument_index = 0):
        if method == 'setItem':
            return '{0}.{1}(arguments[{2}], arguments[{3}])'.format('sessionStorage', method, argument_index, argument_index+1)
        return '{0}.{1}(arguments[{2}])'.format('sessionStorage', method, argument_index)
    
    def key(self, index):
        index = int(index)
        return self.driver.execute_script(
                'return '+self.xScript(method = 'key'), 
                index
                )
        
    def getItem(self, keyname):
        return self.driver.execute_script(
                'return '+self.xScript(method = 'getItem'), 
                keyname
                )
        
    def setItem(self, keyname, value):
        self.driver.execute_script(
                self.xScript(method = 'setItem'), 
                keyname, 
                value
                )
    
    def removeItem(self, keyname):
        self.driver.execute_script(
                self.xScript(method = 'removeItem'),
                keyname
                )
    
    def clear(self):
        self.driver.execute(
                self.xScript(method = 'clear'),
                None
                )
        