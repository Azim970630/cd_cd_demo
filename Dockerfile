FROM python:3.10-slim

WORKDIR /app

COPY requirements/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ app/
COPY tests/ tests/

EXPOSE 8080
ENV PORT=8080
ENV HOST=0.0.0.0

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--worker-class", "sync", "--workers", "1", "app.main:app"]