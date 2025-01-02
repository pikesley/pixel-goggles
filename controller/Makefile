PROJECT = $(shell basename $$(pwd))

build:
	docker build \
		--build-arg ID=${PROJECT} \
		--tag ${PROJECT} .

run:
	docker run \
		--name ${PROJECT} \
		--hostname ${PROJECT} \
		--volume $(shell pwd):/opt/${PROJECT} \
		--publish 8000:80 \
		--interactive \
		--tty \
		--rm \
		${PROJECT} \
		bash
