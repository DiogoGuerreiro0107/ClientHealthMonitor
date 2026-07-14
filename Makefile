.PHONY: help install-backend run-backend migrate makemigrations test-backend shell createsuperuser check format lint

BACKEND_DIR=backend
PYTHON=python

help:
	@echo "Available commands:"
	@echo "  make install-backend   Install backend development dependencies"
	@echo "  make run-backend       Run Django development server"
	@echo "  make migrate           Apply database migrations"
	@echo "  make makemigrations    Create database migrations"
	@echo "  make test-backend      Run backend tests"
	@echo "  make shell             Open Django shell"
	@echo "  make createsuperuser   Create Django superuser"
	@echo "  make check             Run Django system checks"
	@echo "  make format            Format backend code"
	@echo "  make lint              Lint backend code"

install-backend:
	cd $(BACKEND_DIR) && $(PYTHON) -m pip install -r requirements/dev.txt

run-backend:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py runserver

migrate:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py migrate

makemigrations:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py makemigrations

test-backend:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py test

shell:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py shell

createsuperuser:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py createsuperuser

check:
	cd $(BACKEND_DIR) && $(PYTHON) manage.py check

format:
	cd $(BACKEND_DIR) && black .

lint:
	cd $(BACKEND_DIR) && ruff check .