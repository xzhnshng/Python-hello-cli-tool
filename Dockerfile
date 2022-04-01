FROM python:3.8-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY ./requirements.txt /app/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
		pip install -r requirements.txt

COPY . /app