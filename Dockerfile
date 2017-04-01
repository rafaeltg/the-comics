FROM python:2.7

MAINTAINER Rafael Thomazi Gonzalez "rthomazigonzalez@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY ./app /app
COPY ./run.py /app

EXPOSE 5000

CMD [ "./run.py" ]