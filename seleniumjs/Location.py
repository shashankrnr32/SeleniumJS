'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_location.asp

Warning : 
'''
class LocationProperty:
    OBJ = 'location'
    HASH = 'hash'
    HOST = 'host'
    HOSTNAME = 'hostname'
    HREF = 'href'
    ORIGIN = 'origin'
    PATHNAME = 'pathname'
    PORT = 'port'
    PROTOCOL = 'protocol'
    SEARCH = 'search'

class LocationMethod:
    ASSIGN = 'assign'
    RELOAD = 'reload'
    REPLACE = 'replace'
    
class Location:
    def __init__(self,driver):
        self.driver = driver
        self.hash = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.HASH))
        self.host = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.HOST))
        self.hostname = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.HOSTNAME))
        self.href = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.HREF))
        self.origin = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.ORIGIN))
        self.pathname = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.PATHNAME))
        self.port = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.PORT))
        self.protocol = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.PROTOCOL))
        self.search = driver.execute_script('return {0}.{1}'.format(LocationProperties.OBJ, LocationProperties.SEARCH))
    
    def xScript(self,method = LocationMethod.RELOAD,argument_index = 0):
        '''
        detail : 
            Method to Generate Script based on the LocationMethod called. 
            This method is named xScript() just to make the methods accessible in alphabetical order
        param:
            method : 
                type : str
                default : 'reload' (ConsoleMethod.RELOAD)
                details : type of console method called
                eg : ConsoleMethod.RELOAD, ConsoleMethod.REPLACE
            argument_index : 
                type : int
                default : 0
                details : index of argument that is passed in execute_script(script,*args)
                eg : 1, 5, 7
        return:
            A string containing a line of code in JS
        '''
        return '{0}.{1}(arguments[{2}])'.format(LocationProperties.OBJ, method, argument_index)
    
    def assign(self,URL):
        self.driver.get(URL)
        self.__init__(self.driver)
    
    def reload(self):
        self.driver.refresh()
        self.__init__(self.driver)
        
    def replace(self,URL):
        self.driver.execute_script(
                self.xScript(LocationMethod.REPLACE),URL
                )
    
    def setProperty(self,prop = LocationProperties.HREF, value='https://www.yahoo.com'):
        self.driver.execute_script('{0}.{1} = {2}'.format(
                LocationProperties.OBJ, prop, value)
                )
        self.__init__(self.driver)
    