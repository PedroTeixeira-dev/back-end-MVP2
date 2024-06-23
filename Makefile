PROJECT_NAME := efood_app
DATABASE_NAME := efood_database
PYTHON_VERSION := 3.12
VENV_NAME := efood-$(PYTHON_VERSION)

.ONESHELL:
.SHELLFLAGS = -e -c

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | sed -e 's/\(\:.*\#\#\)/\:\ /' | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean: ## remove Python file artifacts
	find . -name '*.pyc' -exec sudo rm -v -f {} +
	find . -name '*.pyo' -exec sudo rm -v -f {} +
	find . -name '*~' -exec sudo rm -v -f {} +
	find . -name '__pycache__' -exec sudo rm -v -fr {} +

setup-dev: ## install dev requirements
	pipenv install --deploy --dev

setup: ## install requirements
	pipenv install --deploy

create-venv: ## install python, create virtualenv and set virtualenv to current
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)
	pip install -U pip pipenv

build: ## up all containers and building the project image
	docker-compose up -d --build

up: ## up all containers
	docker-compose --env-file docker-compose.env up -d --remove-orphans

down: ## down all containers
	docker-compose down
	docker-compose rm

recreate: down up ## recreate containers

init: ## create alembic migratrion structure
	docker exec -it $(PROJECT_NAME) flask db init

migrate: ## create alembic migratrion file
	docker exec -it $(PROJECT_NAME) flask db migrate

upgrade: ## run migratrion
	docker exec -it $(PROJECT_NAME) flask db upgrade

sh: ## run sh inside container
	docker exec -it $(PROJECT_NAME) sh

logs: ## project logs on container
	docker logs $(PROJECT_NAME) --follow

ruff: ## run ruff
	ruff check src
	ruff format src

