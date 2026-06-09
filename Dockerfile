FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata
ENV PYTHONUNBUFFERED=1

RUN apt-get update && 
apt-get install -y tzdata && 
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && 
echo $TZ > /etc/timezone

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN playwright install chromium

EXPOSE 10000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
