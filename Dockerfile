FROM python:latest

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "app.py"]
