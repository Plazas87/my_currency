-include .env
export
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
#----------Tests----------#
# target: test - Run all available test
.PHONY: tests
tests:
	poetry run pytest --cov=src --cov-report=html --cov-report=term tests/
