'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_storage.asp
https://www.w3schools.com/jsref/prop_win_sessionstorage.asp
'''
class StorageMethod:
    OBJ_LOCAL = 'localStorage'
    OBJ_SESSION = 'sessionStorage'
    KEY = 'key'
    GETITEM = 'getItem'
    SETITEM = 'setItem'
    REMOVEITEM = 'removeItem'
    CLEAR = 'clear'
   
class LocalStorage:
    def __init__(self,driver):
        self.driver = driver
        self.length = driver.execute_script('return localstorage.length')

    def xScript(self, method = StorageMethod.KEY, argument_index = 0):
        '''
        detail : 
            Method to Generate Script based on the StorageMethod called. 
            This method is named xScript() just to make the methods accessible in alphabetical order
        param:
            method : 
                type : str
                default : 'key' (StorageMethod.KEY)
                details : type of LocalStorage method called
                eg : StorageMethod.KEY, StorageMethod.GETITEM
            argument_index : 
                type : int
                default : 0
                details : index of argument that is passed in execute_script(script,*args)
                            The 2nd argument takes the argument value = argument_index+1
                eg : 1, 5, 7
        return:
            A string containing a line of code in JS
        '''
        if method == StorageMethod.SETITEM:
            return '{0}.{1}(arguments[{2}], arguments[{3}])'.format(StorageMethod.OBJ_LOCAL, method, argument_index, argument_index+1)
        return '{0}.{1}(arguments[{2}])'.format(StorageMethod.OBJ_LOCAL, method, argument_index)
    
    def key(self, index):
        index = int(index)
        return self.driver.execute_script(
                'return '+self.xScript(method = StorageMethod.KEY), 
                index
                )
        
    def getItem(self, keyname):
        return self.driver.execute_script(
                'return '+self.xScript(method = StorageMethod.GETITEM), 
                keyname
                )
        
    def setItem(self, keyname, value):
        self.driver.execute_script(
                self.xScript(method = StorageMethod.SETITEM), 
                keyname, 
                value
                )
        self.__init__(self.driver)
    
    def removeItem(self, keyname):
        self.driver.execute_script(
                self.xScript(method = StorageMethod.REMOVEITEM),
                keyname
                )
        self.__init__(self.driver)

    def clear(self):
        self.driver.execute(
                self.xScript(method = StorageMethod.CLEAR),
                None
                )
        self.length = 0
        
class SessionStorage:
    def __init__(self,driver):
        self.driver = driver
        self.length = driver.execute_script('return sessionStorage.length')

    def xScript(self, method = StorageMethod.KEY, argument_index = 0):
        '''
        detail : 
            Method to Generate Script based on the StorageMethod called. 
            This method is named xScript() just to make the methods accessible in alphabetical order
        param:
            method : 
                type : str
                default : 'key' (StorageMethod.KEY)
                details : type of LocalStorage method called
                eg : StorageMethod.KEY, StorageMethod.GETITEM
            argument_index : 
                type : int
                default : 0
                details : index of argument that is passed in execute_script(script,*args)
                            The 2nd argument takes the argument value = argument_index+1
                eg : 1, 5, 7
        return:
            A string containing a line of code in JS
        '''
        if method == StorageMethod.SETITEM:
            return '{0}.{1}(arguments[{2}], arguments[{3}])'.format(StorageMethod.OBJ_SESSION, method, argument_index, argument_index+1)
        return '{0}.{1}(arguments[{2}])'.format(StorageMethod.OBJ_SESSION, method, argument_index)
    
    def key(self, index):
        index = int(index)
        return self.driver.execute_script(
                'return '+self.xScript(method = StorageMethod.KEY), 
                index
                )
        
    def getItem(self, keyname):
        return self.driver.execute_script(
                'return '+self.xScript(method = StorageMethod.GETITEM), 
                keyname
                )
        
    def setItem(self, keyname, value):
        self.driver.execute_script(
                self.xScript(method = StorageMethod.SETITEM), 
                keyname, 
                value
                )
        self.__init__(self.driver)
    
    def removeItem(self, keyname):
        self.driver.execute_script(
                self.xScript(method = StorageMethod.REMOVEITEM),
                keyname
                )
        self.__init__(self.driver)

    def clear(self):
        self.driver.execute_script(
                self.xScript(method = StorageMethod.CLEAR)
                )
        self.length = 0