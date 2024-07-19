FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]