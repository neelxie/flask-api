# flask-api

[![Build Status](https://travis-ci.org/neelxie/flask-api.svg?branch=develop)](https://travis-ci.org/neelxie/flask-api)[![Maintainability](https://api.codeclimate.com/v1/badges/c1159a79ad17c21bb8f4/maintainability)](https://codeclimate.com/github/neelxie/flask-api/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/c1159a79ad17c21bb8f4/test_coverage)](https://codeclimate.com/github/neelxie/flask-api/test_coverage)[![Coverage Status](https://coveralls.io/repos/github/neelxie/flask-api/badge.svg?branch=develop)](https://coveralls.io/github/neelxie/flask-api?branch=develop)

Flask Application Programming Interface for my Store-Manager project.

## Heroku Endpoints
|Endpoint|Link|
|Index Route|[/](https://mystoremanager-api.herokuapp.com)|
|'Products' GET|[/storemanager/api/v1/Products](https://mystoremanager-api.herokuapp.com/storemanager/api/v1/Products)|
|'Products' GET Item|[/storemanager/api/v1/Products/name](https://mystoremanager-api.herokuapp.com/storemanager/api/v1/Products/soaks)|
|'Products' POST|[/storemanager/api/v1/Products](https://mystoremanager-api.herokuapp.com/storemanager/api/v1/Products)|
|'Sales' GET |[/storemanager/api/v1/Sales](https://mystoremanager-api.herokuapp.com/storemanager/api/v1/Sales)|
|'Sales' GET |[/storemanager/api/v1/Sales/sale_id](https://mystoremanager-api.herokuapp.com/storemanager/api/v1/Sales/1)|
|'Sales' POST |[/storemanager/api/v1/Sales](https://mystoremanager-api.herokuapp.com/storemanager/api/v1/Sales)|


## Features
 |---|---|
 |- add attendant|
 |- make sales| - add new, modify and delete products|
 |- view user profile|- view sales made by different attendants|
 |- add products to cart|
 ||- view product details|
 

## Project Installation
|Action|Command Neeeded|
|---|---|
|To Install|' git clone https://github.com/neelxie/flask-api.git'|

### Using the project
|Action|Command Needed|
|---|---|
|Project root| 'cd flask-api'|
|Environment creation| 'virtualenv fenv'
|Activate Environment on Windows|' fenv\Scripts\activate'
|Install project Dependencies|' pip install -r requirements.txt|

### Testing the app
- 'pytest' 

### Running the app

- 'python run.py'

### CREDITS
- I would like to appreciate other bootcamp candidates for your efforts in helping me where you could.
## Author
- SEKIDDE DERRICK