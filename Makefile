prepare:
	make migrations
	make migrate
#Si se rompe esto, sacar las foreing keys de la tabla customers a routines, hacer una primer pasada y despues habilitarlas

run:
	make migrate
	pipenv run python manage.py runserver

migrate:
	pipenv run python manage.py migrate
	pipenv run python manage.py migrate sections
	
migrations:
	pipenv run python manage.py makemigrations sections

run-site:
	docker compose up -d --remove-orphans