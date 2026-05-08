FROM python:3.11-slim
# FROM python:3.9.0-slim 
# Set environment variables
# PYTHONDONTWRITEBYTECODE prevents Python from writing .pyc files to disk
# PYTHONUNBUFFERED prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN adduser --disabled-password --gecos '' devsecopsuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER devsecopsuser
EXPOSE 5000
CMD ["python", "app/main.py"]
