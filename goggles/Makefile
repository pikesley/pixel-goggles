default: format test export-controller-data clean

render:
	rm -fr renders/
	python renderer.py

format:
	ruff format
	ruff check --fix

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .ruff_cache -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

test: export TEST = 1
test:
	python -m pytest \
		--random-order \
		--verbose \
		--capture no \
		--exitfirst \
		--last-failed

export-controller-data:
	python export_controller_data.py
