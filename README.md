
# SeleniumJS

>v1.0.12 Beta

Execute Javascript code with selenium.webdriver easily without the need of execute_script(#). Currently supports 5 DOM Objects and a lot more coming to the project soon.

## Currently Supporting  DOM Objects
	
1. [console](https://www.w3schools.com/jsref/obj_console.asp)
2. [location](https://www.w3schools.com/jsref/obj_location.asp)
3. [storage](https://developer.mozilla.org/en-US/docs/Web/API/Storage)
4. [history](https://www.w3schools.com/jsref/obj_history.asp)
5. [navigator](https://www.w3schools.com/jsref/obj_navigator.asp)
## Install
1. To Install using pip

		pip install seleniumjs

2. Steps to install to your project directory

	1. Clone the project to your project directory
	2. run the command `python3 setup.py install`

## Usage
1. **Console Class**
	
	<details>
		<summary>Properties and Methods Supported</summary>
	
	*Properties* :
			
	*Methods* :
	
		console.clear()
		console.count(label = None)
		console.countReset(label = None)
		console.error(message)
		console.group(label = None)
		console.groupCollapsed(label = None)
		console.groupEnd(label = None)
		console.info(message)
		console.log(message)
		console.table(object)
		console.time(label = None)
		console.timeEnd(label = None)
		console.timeLog(label = None)
		console.trace(label = None)
		console.warn(message)
	</details>

	```python
	from seleniumjs import Console
	console = Console(driver)
	console.time()
	console.log('Hello World')
	console.log('This is seleniumjs')
	console.timeEnd()
	```
 
2. **Location Class**

	<details>
			<summary>Properties and Methods Supported</summary>
		
	*Properties* :

		location.hash
		location.host
		location.hostname
		location.href
		location.origin
		location.pathname
		location.port
		location.protocol
		location.search
	*Methods* : 
	
		location.assign(URL)
		location.reload()
		location.replace(URL)
	</details>
	
	```python
	from seleniumjs import Location
	location = Location(driver)
	print(location.href)
	location.href = 'https://github.com/shashankrnr32/SeleniumJS#usage'
	print(location.hash)
	```
	
3. **Storage Module**
	<details>
			<summary>Properties and Methods Supported</summary>
	*Classes*
		LocalStorage
		SessionStorage
		
	*Properties* :

		sessionStorage.length
	*Methods* : 
	
		sessionStorage.key(n)
		sessionStorage.getItem(keyname)
		sessionStorage.setItem(keyname, value)
		sessionStorage.removeItem(keyname)
		sessionStorage.clear()
		
	</details>
	
	```python
	from seleniumjs import SessionStorage
	sessionStorage = SessionStorage(driver)
	sessionStorage.setItem('key', 'value')
	print(sessionStorage.length)
	```
	
	**Info** : Use `LocalStorage` instead of `SessionStorage`

4. **History Class**

	```python
	from seleniumjs import History
	history = History(driver)
	print(history.length)
	history.back()
	print(history.length)
	```
5. **Navigator Class**

	```python
	from seleniumjs import Navigator
	navigator = Navigator(driver)
	print(navigator.appCodeName)
	print(navigator.language)
	```
	**Warning** : `Navigator` doesnt support `geolocation`(yet)
## Testing

The package is under development with testing being done in [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/) and [Mozilla Firefox](https://github.com/mozilla/geckodriver/). Project will be tested in Edge, Opera in the future releases. Contribute to this project by testing it in Safari. 

## License
MIT Free License held by [Shashank Sharma](mailto:shashankrnr32@gmail.com)

This project is not funded/supported by Selenium. To know more about SeleniumHQ visit [here](https://www.seleniumhq.org/)