# Use a slim, secure base image
FROM python:3.11-slim

# Set environment variables
# PYTHONDONTWRITEBYTECODE prevents Python from writing .pyc files to disk
# PYTHONUNBUFFERED prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Create a non-root user for better security 
# (Trivy will flag containers running as root as a vulnerability)
RUN adduser --disabled-password --gecos '' devsecopsuser

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Switch to the non-root user
USER devsecopsuser

# Expose the API port
EXPOSE 5000

# Command to run the application
CMD ["python", "app/main.py"]
