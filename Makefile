.PHONY: lint test exec

lint:
	poetry run black .

test:
	poetry run

exec:
	docker-compose exec scheduler bash
