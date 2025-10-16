install:
	poetry install

project:
	poetry run labyrinth

lint:
	poetry run ruff check .

build:
	poetry build