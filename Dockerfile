FROM python:3.8-slim-buster

WORKDIR /src

COPY /src/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV PYTHONPATH /src
COPY . .
CMD ["python3", "./src/main.py"]