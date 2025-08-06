# Start from a base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our application code
COPY . .

# Tell Docker what command to run when the container starts
CMD ["python", "app.py"]
