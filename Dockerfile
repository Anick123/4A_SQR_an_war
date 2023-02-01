FROM python:3.8

RUN apt-get upgrade
RUN apt-get update 
RUN apt-get install python3-pip -y

COPY . .
ENV FLASK_APP=firstversion_API.py
ENV FLASK_DEBUG=True

EXPOSE 5000


CMD [ "flask", "run" ]
