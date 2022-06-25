run:
	python3 manage.py runserver

makemigrate:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

full migrate:
	python3 manage.py makemigrations && python3 manage.py migrate

staticfiles:
	python3 manage.py collectstatic

copydata:
	python3 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > db.json

loaddata:
	python3 manage.py loaddata db.json

push: 
	git add . && git commit --amend && git push -f origin feature/models && git push heroku master