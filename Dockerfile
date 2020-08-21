FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
#EXPOSE 8000
#CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:8000