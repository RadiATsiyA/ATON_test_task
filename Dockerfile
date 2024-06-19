# Pull base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /ATON-test

# Install dependencies
COPY requirements.txt /ATON-test/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /ATON-test/