FROM python:3.8-slim-buster
WORKDIR /app

COPY . .

CMD [ "python", "dummy_app.py" ]