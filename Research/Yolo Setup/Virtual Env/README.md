# VIRTUAL ENVIRONMENT IN PYTHON
------

this script follows a standard procedure to making a new virtual environment using python in windows

## Creating the Virtual Env
------
to install the virtual environment package to main Python branch:
```
	python -m pip install --user virtual env
```
To create the Python Virtual Env named: "my_env_name":
```
	python -m venv my_env_name
```
Activating the Virtual Env:
```
	.\my_env_name\scripts\activate
```

## Installing Dependencies 
------
before installing anything you need to go inside the virtual environment folder and inside the configuration file called: "pyvenv.cfg" change the line `include-system-site-packages = false` to `include-system-site-packages = true`. 

Upgrade Pip:
```
	pip install --upgrade pip
```

installing new packages: 
```
	pip install -U --force-reinstall package_name
```

## Installing Jupyter Notebook (Optional)
------
Install Jupyter Notebook:
```
	pip install -U --force-reinstall jupyter
```
for jupyter, note that you'll need to add the virtual enviornment to jupyter notebook using the command 
```
	python -m ipykernel install --user --name=my_env_name
```
also if you want to later remove this kernel from jupyter notebook just use the command:
```
	python -m jupyter kernelspec uninstall my_env_name
```
