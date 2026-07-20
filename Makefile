# This is our list of "phony" targets (command names).
.PHONY: run makemigrations migrate shell test

run:
	# This line MUST be indented with a TAB, not spaces!
	uv run python manage.py runserver

makemigrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

createsuperuser:
	uv run python manage.py createsuperuser


	