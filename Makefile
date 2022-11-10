fail-if-no-virtualenv:
ifndef VIRTUAL_ENV # check for a virtualenv in development environment
$(error this makefile needs a virtualenv)
endif

install: fail-if-no-virtualenv
	pip install .[test]

black: fail-if-no-virtualenv
	@black --config pyproject.toml secret_gen

lint: fail-if-no-virtualenv
	black --check --config pyproject.toml secret_gen
	pylint secret_gen



