# SeleniumJS

>v1.0.11

Execute Javascript code with selenium.webdriver easily without the need of execute_script(#). Currently supports 5 DOM Objects and a lot more coming to the project soon.

## Currently Supporting  DOM Objects
	
1. [console](https://www.w3schools.com/jsref/obj_console.asp)
2. [location](https://www.w3schools.com/jsref/obj_location.asp)
3. [sessionStorage](https://www.w3schools.com/jsref/prop_win_sessionstorage.asp)
4. [localStorage](https://www.w3schools.com/jsref/obj_storage.asp)
5. [history](https://www.w3schools.com/jsref/obj_history.asp)
## Install
1. To Install using pip

		pip install seleniumjs

2. Steps to install to your project directory

	1. Clone the project to your project directory
	2. run the command `python3 setup.py install`

## Usage
1. **Console Class**

	```python
	from seleniumjs import Console
	console = Console(driver)
	console.time()
	console.log('Hello World')
	console.log('This is seleniumjs')
	console.timeEnd()
	```
	**Warning** : `Console` doesnt support `assert` method
	
 
2. **Location Class**

	```python
	from seleniumjs import Location
	location = Location(driver)
	print(location.href)
	location.href = 'https://github.com/shashankrnr32/SeleniumJS#usage'
	print(location.hash)
	```
	
3. **Storage Class**
	
	```python
	from seleniumjs import SessionStorage
	sessionStorage = SessionStorage(driver)
	sessionStorage.setItem('key', 'value')
	print(sessionStorage.length)
	```
	
	**Info** : Use `LocalStorage` instead of `SessionStorage`

4. **History**

	```python
	from seleniumjs import History
	history = History(driver)
	print(history.length)
	history.back()
	print(history.length)
	```
	
## License
MIT Free License held by [Shashank Sharma](mailto:shashankrnr32@gmail.com)

This project is not funded/supported by Selenium. To know more about SeleniumHQ visit [here](https://www.seleniumhq.org/)