'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_console.asp

Warning : console.assert() is not supported in this package.
'''
class ConsoleMethod:
    OBJ = 'console'
    CLEAR = 'clear'
    COUNT = 'count'
    ERROR = 'error'
    GROUP = 'group'
    GROUPCOLLAPSED = 'groupCollapsed'
    GROUPEND = 'groupEnd'
    INFO = 'info'
    LOG = 'log'
    TABLE = 'table'
    TIME = 'time'
    TIMEEND = 'timeEnd'
    TRACE = 'trace'
    WARN = 'warn'
    
   
class Console:    
    def __init__(self, driver):
        self.driver = driver
        
    def xScript(self ,method=ConsoleMethod.LOG, argument_index = 0):
        '''
        detail : 
            Method to Generate Script based on the ConsoleMethod called. 
            This method is named xScript() just to make the methods accessible in alphabetical order
        param:
            method : 
                type : str
                default : 'log' (ConsoleMethod.LOG)
                details : type of console method called
                eg : ConsoleMethod.LOG, ConsoleMethod.CLEAR
            argument_index : 
                type : int
                default : 0
                details : index of argument that is passed in execute_script(script,*args)
                eg : 1, 5, 7
        return:
            A string containing a line of code in JS
        '''
        return '{0}.{1}(arguments[{2}]);'.format(ConsoleMethod.OBJ, method, argument_index)
    
    def clear(self):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.CLEAR)
                )
    
    def count(self, label=None):
        if not label : 
            label = 'default'
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.COUNT), 
                label
                )
    
    def error(self, message):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.ERROR), 
                message
                )
    
    def group(self, label = None):
        if not label : 
            label = '{0}.{1}'.format(
                    ConsoleMethod.OBJ, 
                    ConsoleMethod.GROUP
                    )
        
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.GROUP), 
                label
                )
        
    def groupCollapsed(self, label = None):
        if not label : 
            label = '{0}.{1}'.format(
                    ConsoleMethod.OBJ, 
                    ConsoleMethod.GROUP
                    )
        
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.GROUPCOLLAPSED), 
                label
                )
    
    def groupEnd(self):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.GROUPEND)
                )
    
    def info(self, message):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.INFO), 
                message
                )
        
    def log(self,message):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.LOG), 
                message
                )
    
    def table(self,tabledata):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.TABLE), 
                tabledata
                )
         
    def time(self,label=None):
        if not label : 
            label = 'default'
            
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.TIME), 
                label
                )
        
    def timeEnd(self,label = None):
        if not label : 
            label = 'default'
        
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.TIMEEND), 
                label
                )
        
    def trace(self, label = None):
        if not label : 
            label = '{0}.{1}'.format(
                    ConsoleMethod.OBJ, 
                    ConsoleMethod.TRACE
                    )
            
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.TRACE), 
                label
                )
        
    def warn(self, message):
        self.driver.execute_script(
                self.xScript(method = ConsoleMethod.WARN), 
                message
                )    

