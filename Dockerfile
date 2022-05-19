FROM python:3.9-alpine
WORKDIR app/src
COPY app/src/requirements.txt .
RUN pip install -r requirements.txt