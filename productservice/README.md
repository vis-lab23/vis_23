# Productservice
is a Django / Django Rest Framework based application

## How to run for debugging
```bash
docker-compose build
docker-compose up -d web-shop-db-image category-service
poetry install  # get python dependencies (if install of mysqlclient fails see https://github.com/PyMySQL/mysqlclient#install for more infos)
cd productmanager/
CATEGORY_SERVICE_HOST=127.0.0.1 ./manage.py migrate # apply database changes
CATEGORY_SERVICE_HOST=127.0.0.1 ./manage.py runserver 127.0.0.1:8000 # start api
```
