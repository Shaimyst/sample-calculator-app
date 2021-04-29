# Sample Calculator Application


## Requirements
 - homebrew
 - pipenv
 - npm


---


## Initial Setup

### npm installs
```sh
npm install
```

### Install chromedriver

```sh
brew cask install chromedriver
```

### Python installs with pipenv

setup pipenv virtual-environment for project:    
```sh
pipenv install
```

spin-up virtual-environment:
```sh
pipenv shell
```

spin-down the virtual-environment:
```sh
exit
```


---


## Spin-up application

Run: `make dev`
  
navigate to `localhost:5000`  
  
spin-down with mac OS key command: `control+c`


---


## Run Selenium tests

```sh
pytest
```