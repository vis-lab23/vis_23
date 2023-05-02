FROM docker.io/library/python:3.9.16-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential
# Allows docker to cache installed dependencies between builds
# poetry export > requirements.txt
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY productmanager code
WORKDIR /code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python manage.py migrate && runserver 0.0.0.0:8000"]
