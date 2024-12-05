ID = $(shell basename $$(pwd))

build:
	docker build \
		--build-arg ID=${ID} \
		--tag ${ID} .

run:
	docker run \
		--name ${ID} \
		--hostname ${ID} \
		--volume $(shell pwd):/opt/${ID} \
		--interactive \
		--tty \
		--rm \
		${ID} \
		bash
