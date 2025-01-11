ID = $(shell basename $$(pwd))

build:
	docker build \
		--build-arg ID=${ID} \
		--tag ${ID} .

run:
	docker run \
		--name ${ID} \
		--hostname ${ID} \
		--workdir /opt/${ID}/goggles \
		--volume $(shell pwd):/opt/${ID} \
		--interactive \
		--tty \
		--rm \
		${ID} \
		bash

reset:
	$(shell echo '{"pattern-index": 0}' > /tmp/state.json)
	python -m mpremote cp /tmp/state.json :

push: reset
	python -m mpremote cp -r goggles/*py :
	python -m mpremote cp -r goggles/lib :
	python -m mpremote cp -r goggles/patterns :
	python -m mpremote cp -r goggles/conf :
	python -m mpremote cp -r vendor :

connect:
	python -m mpremote

.PHONY: renders
renders:
	python -m mpremote cp -r goggles/renders :

nuke:
	python -m esptool \
		--chip esp32c3 \
		erase_flash

flash:
	python -m esptool \
		--chip esp32c3 \
		write_flash \
		0x0 \
		../esp32-firmware/c3-current

reinstall: nuke flash install-aioble push renders connect

install-aioble:
	rm -fr /tmp/micropython
	git clone https://github.com/micropython/micropython-lib.git /tmp/micropython

	rm -fr /tmp/micropython/micropython/bluetooth/aioble/multitests/
	rm -fr /tmp/micropython/micropython/bluetooth/aioble/examples/

	mkdir -p vendor
	rsync -av /tmp/micropython/micropython/bluetooth/aioble vendor/
