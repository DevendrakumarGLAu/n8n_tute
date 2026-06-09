FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && 
apt-get install -y tzdata && 
ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && 
dpkg-reconfigure --frontend noninteractive tzdata

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN playwright install chromium

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
