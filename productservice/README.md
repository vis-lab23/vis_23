# Productservice
is a Django / Django Rest Framework based application

## How to run for debugging
```bash
docker-compose build
docker-compose up -d web-shop-db-image category-service  # start dependencies (DB, category service)
poetry install  # get python dependencies (if install of mysqlclient fails see https://github.com/PyMySQL/mysqlclient#install for more infos)
cd productmanager/
CUSTOM_CATEGORY_SERVICE_HOST=127.0.0.1 ./manage.py migrate # apply database changes
CUSTOM_CATEGORY_SERVICE_HOST=127.0.0.1 ./manage.py runserver 127.0.0.1:8000 # start api
```

## OpenAPI Schema
* [OpenAPI UI](http://127.0.0.1:8000/openapi-ui/)
* [OpenAPI JSON](http://127.0.0.1:8000/openapi/?format=openapi-json)
* [OpenAPI YAML](http://127.0.0.1:8000/openapi/)
