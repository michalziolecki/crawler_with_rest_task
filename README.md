# Microservice with RESTful API and scraper #

author MZ

### Technology stack ###
Python 3.9, Django, DRF, DjangoORM, Request, BeautifulSoup, Git + Git Flow, Swagger(Open API 2.0), Pytest, Docker

### Requirements ###
* Python3.9
* Unoccupied port 8000

### Prepare virtualenv (Linux) ###

* Prepare directory for virtual env (on the root of project):
	`mkdir venv`
* Prepare virtual env module:
	`sudo apt-get install python3-venv`
* Create venv:
	`python3.9 -m venv ./venv/`
* Checkout to venv:
	`source ./venv/bin/activate`
* Install requirements:
	`pip install -r requirements`
* Check requirements:
	`pip freeze`
* Default python 3.6 if You want:
	`alias python=/usr/bin/python3.9`

### Run application locally ###

* Source the virtaul enviroment:
	`source ./vevn/bin/activate`
* Install requirements (if aren't installed):
	`pip install -r requirements`
* Migrate:
	`python3.9 manage.py migrate`
* Run django application:
	`python3.9 manage.py runserver`

### Run tests ###

* Command to run all test (from directory with manage.py):
	* `pytest scraper`
	* `pytest restful_api/simple_rest_api/`

### Run with Docker ###

* Build image (run from directory with Dockerfile)
	`docker build -t scraper_api .`
* Run container:
	`docker run -d -p 8000:8000 scraper_api` or `docker run -p 8000:8000 scraper_api`
* Check running process, after detach (-d):
	`docker container ps`
* Stop container if is detached:
	`docker stop container <sha_id>`
