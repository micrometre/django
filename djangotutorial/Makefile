.PHONY: run
db_init:
	python manage.py migrate
serve:
	python manage.py runserver 0.0.0.0:8000

curl_data:
	curl -X POST -H "Content-Type: application/json" -d @data.json 127.0.0.1:8080/items