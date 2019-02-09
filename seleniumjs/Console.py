'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_console.asp

Warning : console.assert() is not supported in this package.
'''
class Console:    
    def __init__(self, driver):
        self.driver = driver
        
    def xScript(self ,method='log', argument_index = 0):
        return '{0}.{1}(arguments[{2}]);'.format('console', method, argument_index)
    
    def clear(self):
        self.driver.execute_script(
                self.xScript(method = 'clear')
                )
    
    def count(self, label=None):
        if not label : 
            label = 'default'
        self.driver.execute_script(
                self.xScript(method = 'count'), 
                label
                )
    
    def countReset(self, label=None):
        if not label : 
            label = 'default'
        self.driver.execute_script(
                self.xScript(method = 'countReset'), 
                label
                )
    
    def error(self, message):
        self.driver.execute_script(
                self.xScript(method = 'error'), 
                message
                )
    
    def group(self, label = None):
        if not label : 
            label = '{0}.{1}'.format(
                    'console', 
                    'group'
                    )
        
        self.driver.execute_script(
                self.xScript(method = 'group'), 
                label
                )
        
    def groupCollapsed(self, label = None):
        if not label : 
            label = '{0}.{1}'.format(
                    'console', 
                    'groupCollapsed'
                    )
        
        self.driver.execute_script(
                self.xScript(method = 'groupCollapsed'), 
                label
                )
    
    def groupEnd(self):
        self.driver.execute_script(
                self.xScript(method = 'groupEnd')
                )
    
    def info(self, message):
        self.driver.execute_script(
                self.xScript(method = 'info'), 
                message
                )
        
    def log(self,message):
        self.driver.execute_script(
                self.xScript(method = 'log'), 
                message
                )
    
    def table(self,tabledata):
        self.driver.execute_script(
                self.xScript(method = 'table'), 
                tabledata
                )
         
    def time(self,label=None):
        if not label : 
            label = 'default'
            
        self.driver.execute_script(
                self.xScript(method = 'time'), 
                label
                )
        
    def timeEnd(self,label = None):
        if not label : 
            label = 'default'
        
        self.driver.execute_script(
                self.xScript(method = 'timeEnd'), 
                label
                )
    
    def timeLog(self,label = None):
        if not label : 
            label = 'default'
        
        self.driver.execute_script(
                self.xScript(method = 'timeLog'), 
                label
                )
   
    def trace(self, label = None):
        if not label : 
            label = '{0}.{1}'.format(
                    'console', 
                    'trace'
                    )
            
        self.driver.execute_script(
                self.xScript(method = 'trace'), 
                label
                )
        
    def warn(self, message):
        self.driver.execute_script(
                self.xScript(method = 'warn'), 
                message
                )    

