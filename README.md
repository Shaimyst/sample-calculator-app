# Sample Calculator Application

## npm Installs
### Package
-------------------------
 - node 14.16.0 or later
 - npm 6.14.11 or later
 - pip 21.0.1 or later
 - python 3.7.3 or later
 - homebrew (mac) 3.1.3 or later  

## sequence of commands to run pipenv
install pipenv:   
```brew install pipenv```  
  
setup pipenv virtual-environment for project:    
```pipenv install```  
  
spin-up virtual-environment  
```pipenv shell```  
  
do python package installs within virtual-environment  
```pipenv install selenium\```  
    (puts selenium in the Pipfile)   


## instructions for installing chromedriver

```brew cask install chromedriver```  
or using npm  
```npm install chromedriver```  

## spin-up application

````make dev````  
  
navigate to `localhost:5000`  
  
spin-down with mac OS key command ````control+c````  

## run all tests through pytest

This will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.  
```pytest```