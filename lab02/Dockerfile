FROM python:3.11-slim

WORKDIR /app
COPY ./app/app.py .
RUN pip install fastapi uvicorn
EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

