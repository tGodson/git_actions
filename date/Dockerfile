FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY date.py .

EXPOSE 8080

CMD ["python", "date.py"]
