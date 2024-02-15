-include .env
export

DJANGO_PRODUCTION_SETTINGS_MODULE = ${DJANGO_SETTINGS_MODULE}
IFACE ?= 127.0.0.1
PORT  ?= 8000

ifeq ($(OS),Windows_NT)
	OPEN_CMD = cmd /c start
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		OPEN_CMD = xdg-open
	endif
	ifeq ($(UNAME_S),Darwin)
		OPEN_CMD = open
	endif
endif

#----------General----------#

# Extract arguments of the subcommand
.PHONY: _run_args
_run_args:
  # use the rest as arguments for the subcommand
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)

# target: help - Display callable targets.
.PHONY: help
help:
	@egrep "^# target:" [Mm]akefile


########-------Django MyCurrency app-------########

#----------Docker Database----------#

# target: initdb - Initialize the database container
.PHONY: initdb
initdb:
	docker run -d --name my_currency_db \
		-v my_currency_data:/var/lib/postgresql/data \
		-p 5432:5432 \
		-e POSTGRES_HOST_AUTH_METHOD=trust \
		postgres:14

# target: createdb - Create the Database
.PHONY: createdb
createdb:
	docker exec -it my_currency_db createdb -U postgres my_currency

# target: startdb - Start a postgres database for the my_currency
.PHONY: startdb
startdb:
	docker start my_currency_db

# target: stopdb - Stop the my_currency postgres database
.PHONY: stopdb
stopdb:
	docker stop my_currency_db


# target: start - Start the apliaction using Docker containers
.PHONY: start
start:
	docker-compose up --build


#----------Tests----------#
# target: test - Run all available test
.PHONY: tests
tests:
	poetry run pytest --cov=src --cov-report=html --cov-report=term tests/

#----------Django commands----------#


# target: clean_pyc - Remove all ".pyc" files
.PHONY: clean_pyc
clean_pyc:
	poetry run python -m my_currency.controllers.manage clean_pyc --path=src/my_currency

# target: createsuperuser - Create a super user account
.PHONY: createsuperuser
createsuperuser:
	poetry run python -m my_currency.controllers.manage createsuperuser

# target: shell_plus - Enter interactive environment
.PHONY: shell_plus
shell_plus:
	poetry run python -m my_currency.controllers.manage shell_plus

# target: make-migrations - Create migration files
.PHONY: make-migrations
make-migrations:
	poetry run python -m my_currency.controllers.manage makemigrations

# target: apply-migrations - Create migration files
.PHONY: apply-migrations
apply-migrations:
	poetry run python -m my_currency.controllers.manage migrate


# target: lstart - Start the application locally
.PHONY: lstart
lstart:
	poetry run python -m my_currency.controllers.manage runserver $(IFACE):$(PORT)

# target: run - Executes any of the available django commands
.PHONY: run
run: _run_args
	poetry run python -m my_currency.controllers.manage $(RUN_ARGS)
