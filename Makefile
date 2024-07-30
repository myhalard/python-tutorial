install:
	python3 -m venv ~/.venv
	. ~/.venv/bin/activate
	pip3 install --upgrade pip && pip3 install -r requirements.txt

format:
	. ~/.venv/bin/activate
	black .

lint:
	. ~/.venv/bin/activate
	pylint --disable=R,C --ignore=.venv $(shell find . -path "./.venv" -prune -o -name "*.py")

test:
	. ~/.venv/bin/activate
	pytest -p no:warnings --nbval --ignore=virtual-envs.ipynb --ignore=fastapi-app.ipynb --ignore=flask-app.ipynb

all: install format lint test