# README
[![Python hello-cli-tool CI/CD with GitHub Action (build image and push image to ECR)](https://github.com/xzhnshng/ids-project2/actions/workflows/main.yml/badge.svg)](https://github.com/xzhnshng/ids-project2/actions/workflows/main.yml)


## Overview
This project is about a Python script deployment based on Kubernetes Continous Delivery.  <br/><br/>

## Project Guideline (IDS 721 individual project2)
Kubernetes based Continuous Delivery
- Create a customized Docker container from the current version of Python that deploys a simple python script.
- Push image to DockerHub, or Cloud based Container Registry (ECR)
- Project should deploy automatically to Kubernetes cluster
- Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)
> Reference Reading:  https://learning.oreilly.com/library/view/python-for-devops/9781492057680/ch09.html#containers-docker </br>
> Reference Source Code: https://github.com/noahgift/container-revolution-devops-microservices

<br/>

## Steps
- Create a Python cli tool
- Containerze: Dockerfile
- GitHub Action perform CI/CD
- ECR
- EKS

## Python hello-cli-tool
tried commands like
$ python app.py
$ python app.py --help
$ python app.py --count=5 --name=”John”
$ python app.py --name=”John”
<img width="714" alt="image" src="https://user-images.githubusercontent.com/47130690/161396855-4ae9d531-0d57-4177-b8ba-23cc0da3c45e.png">



## Dockerfile
```Dockerfile
FROM python:3.8-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY ./requirements.txt /app/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
		pip install -r requirements.txt

COPY . /app
```

## play with hello-cli-tool container demo
#### Option 1: Run it yourself (in a bash terminal inside the container)
use this command to start a bash shell in the container
`$ docker run --rm -it hello-cli-tool:v1.0 bash`
then you can run the app.py with parameters as how you did in local terminal
e.g.,
`$ python app.py --count 3 --name “John”`
which is same as `$ python app.py --count=3 --name=“John”`

e.g.,
`$ python app.py`

To exit the bash terminal, type `exit`

#### Option 2: Pass in a command
`$ docker run --rm -it hello-cli-tool:v1.0 python app.py --count 2 --name "John"`
or
`$ docker run --rm -it hello-cli-tool:v1.0 python app.py --name="John"
or
`$ docker run --rm -it hello-cli-tool:v1.0 python app.py --count 2` 


## GitHub Action continuous deployment
<img width="436" alt="image" src="https://user-images.githubusercontent.com/47130690/161396731-3619b31f-d4ac-423e-b017-8b1ad13ba9da.png">
<img width="455" alt="image" src="https://user-images.githubusercontent.com/47130690/161396702-2cdf3247-e796-4022-9ee8-805ef4401926.png">
<img width="1387" alt="image" src="https://user-images.githubusercontent.com/47130690/161396650-cd8c23fd-4b81-4de7-9a21-30358d428568.png">



