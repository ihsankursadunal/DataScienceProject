FROM python:3.9-slim-buster
LABEL maintainer="Ihsan Kursad Unal"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN useradd -ms /bin/bash user
USER user

EXPOSE 8000

CMD [ "python", "/app/manage.py", "runserver", "0.0.0.0:8000"]