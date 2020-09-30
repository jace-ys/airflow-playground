.PHONY: all fmt test image exec

all: fmt test

fmt:
	poetry run black .

test:
	poetry run python -m pytest -v test

image:
	docker build -t airflow-playground:latest .

exec:
	docker-compose exec scheduler bash
