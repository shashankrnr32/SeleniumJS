# SeleniumJS

Execute Javascript code as it is without having to use execute_script() of the selenium library. Refer to DOM objects.

## Currently Supporting  DOM Objects
	
1. [console](https://www.w3schools.com/jsref/obj_console.asp)
2. [location](https://www.w3schools.com/jsref/obj_location.asp)
3. [sessionStorage](https://www.w3schools.com/jsref/prop_win_sessionstorage.asp)
4. [localStorage](https://www.w3schools.com/jsref/obj_storage.asp)

## Install
To Install using pip

	pip install -i https://test.pypi.org/simple/ seleniumjs

Steps to install to your project directory

1. Clone the project to your project directory
2. run the command `python3 setup.py install`

## Usage
#### Usage of Console Class 

```python
	from seleniumjs.Console import Console
	console = Console(driver)
	console.time()
	console.log('Hello World!!')
	console.timeEnd()
```
> **Warning** : Console class does not support assert function

#### Usage of Location Class
	
```python
	from seleniumjs.Location import Location
	location = Location(driver)
	print(location.href)

	from seleniumjs.Location import LocationProperty
	location.setProperty(LocationProperty.HASH,'id_value')
```	
		
#### Usage of LocalStorage/SessionStorage
```python
	from seleniumjs.Storage import SessionStorage
	#import LocalStorage instead of SessionStorage
	sessionStorage = SessionStorage(driver)
	
	print(sessionStorage.length)
	sessionStorage.getItem('key', 'value')
```

## License
MIT Free License held by [Shashank Sharma](mailto:shashankrnr32@gmail.com)

This project is not funded/supported by Selenium. To know more about SeleniumHQ visit [here](https://www.seleniumhq.org/)