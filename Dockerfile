FROM ubuntu
FROM python:3

ADD FirstProgram.py .

RUN apt-get update -y

RUN apt-get install -y python-dev build-essential

CMD ["python", "FirstProgram.py"]
