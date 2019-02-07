# SeleniumJS

Execute Javascript code as it is without having to use execute_script() of the selenium library. Refer to DOM objects.

## Currently Supporting  DOM Objects
	
1. [console](https://www.w3schools.com/jsref/obj_console.asp)
2. [location](https://www.w3schools.com/jsref/obj_location.asp)

## Install
Install instructions coming soon as setup.py is yet to be updated. Use the package now by copying the `seleniumjs` folder to your project directory

## Usage
1. Usage of Console Class 

		from seleniumjs.Console import Console
		console = Console(driver)
		console.time()
		console.log('Hello World!!')
		console.timeEnd()
	> **Warning** : Console class does not support assert function

2. Usage of Location Class

		from seleniumjs.Location import Location
		location = Location(driver)
		print(location.href)
	
		from seleniumjs.Location import LocationProperty
		location.setProperty(LocationProperty.HASH,'id_value')

## License
MIT Free License held by [Shashank Sharma](mailto:shashankrnr32@gmail.com)