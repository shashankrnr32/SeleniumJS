'''
Developer : Shashank Sharma
License : MIT Free License 
Reference : https://www.w3schools.com/jsref/obj_location.asp
'''
class Location:
    def __init__(self,driver):
        self.driver = driver
        self._href = self.href
        
    def xScript(self,method = 'reload',argument_index = 0):
        return '{0}.{1}(arguments[{2}]);'.format('location', method, argument_index)
    
    def assign(self,URL):
        self.driver.get(URL)
        
    def reload(self):
        self.driver.refresh()
            
    def replace(self,URL):
        self.driver.execute_script(
                self.xScript('replace'),URL
                )
    
    @property
    def hash(self):
        return self.driver.execute_script('return location.hash;')
    
    @hash.setter
    def hash(self,anchorname):
        self.driver.execute_script('location.hash = \'{}\''.format(anchorname))
       
    @property   
    def host(self):
        return self.driver.execute_script('return location.host')
    
    @host.setter
    def host(self, host):
        self.driver.execute_script('location.host = \'{}\''.format(host))
        
    @property
    def hostname(self):
        return self.driver.execute_script('return location.hostname')
    
    @hostname.setter
    def hostname(self, hostname):
        self.driver.execute_script('location.hostname = \'{}\''.format(hostname))
        
    @property
    def href(self):
        self._href = self.driver.execute_script('return location.href')
        return self._href
    
    @href.setter
    def href(self, URL):
        self._href = self.driver.execute_script('location.href = \'{}\''.format(URL))
    
    @property
    def origin(self):
        self.driver.execute_script('return location.origin')
        
    @origin.setter
    def origin(self, origin):
        self.driver.execute_script('location.origin = \'{}\''.format(origin))
        
    @property
    def pathname(self):
        return self.driver.execute_script('return location.pathname')
        
    @pathname.setter
    def pathname(self, pathname):
        self.driver.execute_script('location.pathname = \'{}\''.format(pathname))
        
    @property
    def port(self):
        return self.driver.execute_script('return loacation.port')
    
    @port.setter
    def port(self, port):
        self.driver.execute_script('location.port = \'{}\''.format(port))
    
    @property
    def protocol(self):
        return self.driver.execute_script('return location.protocol')
    
    @protocol.setter
    def protocol(self, protocol):
        self.driver.execute_script('location.protocol = \'{}\''.format(protocol))
        
    @property
    def search(self):
        return self.driver.execute_script('return loacation.protocol')
    
    @search.setter
    def search(self, search):
        self.driver.execute_script('location.search = \'{}\''.format(search))