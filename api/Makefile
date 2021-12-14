NAME = ev-charger-cost-calc-api
CWD = $(shell pwd)
VERSION = 0.1.0
build:
	docker build -t $(NAME):$(VERSION) --rm .

build-nocache:
	docker build -t $(NAME):$(VERSION) --no-cache --rm .

remove:
	docker image rm $(NAME):$(VERSION) 

run-dev:
	docker run -it --rm -p 8000:8000 -v "$(CWD)/app/app":"/app" $(NAME):$(VERSION) bash

run-prod:
	docker run -it --rm $(NAME):$(VERSION) bash
