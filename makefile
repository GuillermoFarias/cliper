.PHONY: test

test:
	pytest --cov=app --cov-report=html tests/