FROM python:3.12

WORKDIR /home/felipe-dutra/botRural

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
