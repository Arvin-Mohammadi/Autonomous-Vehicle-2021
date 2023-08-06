# VIRTUAL ENVIRONMENT IN PYTHON

this script follows a standard procedure to making a new virtual environment using python in windows and linux

## Creating the Virtual Env

if needed first use the following command 
```
	pip install --user virtual env
```
then to create the virtual environemnt you can use: 
```
	python -m venv my_env_name
```
now for activating the virtual environment type: 
```
	.\my_env_name\scripts\activate
```

## Installing Dependencies 

before installing anything you need to go inside the virtual environment folder and inside the configuration file called: "pyvenv.cfg" change the line: 
```
	include-system-site-packages = false
```
to 
```
	include-system-site-packages = true
```
then you need to upgrade pip and the command for that is:
```
	pip install --upgrade pip
```
after these steps there shouldn't be a warning or error and you'll be able to install the dependencies using the command: 
```
	pip install -U --force-reinstall package_name
```

## Most Used packages for installing 

There are a couple of packages that you'll most likely be needing are `numpy` and `jupyter` and `pandas` and `matplotlib` and etc.
for jupyter note that you'll need to add the virtual enviornment to jupyter notebook using the command 
```
	python -m ipykernel install --user --name=my_env_name
```
also if you want to later remove this kernel from jupyter notebook just use the command:
```
	python -m jupyter kernelspec uninstall my_env_name
```
