# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Copy the rest of the application code into the container
COPY . .

RUN chmod +x start_app.sh


CMD ["./start_app.sh"]
