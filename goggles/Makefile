default: format test export-controller-data clean

reset:
	$(shell echo '{"pattern-index": 0}' > /tmp/state.json)
	python -m mpremote cp /tmp/state.json :

push: reset
	python -m mpremote cp -r *py :
	python -m mpremote cp -r lib :
	python -m mpremote cp -r patterns :
	python -m mpremote cp -r vendor :

render:
	rm -fr renders/
	python renderer.py

.PHONY: renders
renders:
	python -m mpremote cp -r renders :

connect:
	python -m mpremote

mount:
	python -m mpremote mount .

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

nuke:
	python -m esptool \
		--chip esp32c3 \
		erase_flash

flash:
	python -m esptool \
		--chip esp32c3 \
		write_flash \
		0x0 \
		../../esp32-firmware/c3-current

reinstall: nuke flash push renders connect

install-aioble:
	rm -fr /tmp/micropython
	git clone https://github.com/micropython/micropython-lib.git /tmp/micropython
	mkdir -p vendor
	rsync -av /tmp/micropython/micropython/bluetooth/aioble vendor/

export-controller-data:
	python export_controller_data.py
