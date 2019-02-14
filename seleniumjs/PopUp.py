'''
Developer : Shashank Sharma
License : MIT Free License
'''

def alert(message, driver):
    driver.execute_script('alert(arguments[0])',message)

def confirm(message, driver):
    return driver.execute_script('return confirm(arguments[0])', message)
    
def prompt(message, defaultText, driver):
    return driver.execute_script('return prompt(arguments[0])', message)