all: push connect

push:
	python -m mpremote cp -r *py :
	python -m mpremote cp -r lib :
	python -m mpremote cp -r conf :

connect:
	python -m mpremote

format:
	ruff format
	ruff check --fix

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .ruff_cache -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;
