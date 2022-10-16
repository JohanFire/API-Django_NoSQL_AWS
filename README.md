# API-Django_NoSQL_AWS

API Rest using Django, NoSQL. DynamoDB in AWS

# Virtual enviroment & dependencies

## Create a virtual env

All dependencies will be created in virtual env

```bash
	python -m venv .venv
```

## Activate virtual env

```bash
	. .venv/Scripts/activate
```

# AWS & DynamoDB

## Install CLI Interface

go to https://aws.amazon.com/es/cli/

## DynamoDB

go to aws and search for DynamoDB.
create IAM user and get credentials.
install CLI 2 in windows or your OS system

### Get credentials

go to AWS, log in and click on user on top bar and go to "Secured Credentials"
create an Access Key ID
and save the Access Key and Secret key or download file

open a terminal and type

```bash
	aws configure
```

and write Access Key credentials
Default region name: us-east-2 (por ejemplo)
Default output format: json

this creates a file inside the user directory called "aws"
and 2 files, "credentials" and "config"
can see content with

```bash
	type credentials
```

# Install dependencies

inside venv of course

```bash
	pip3 install django django-rest-framework
```

# Start Django project

django-admin startproject NAME_PROJECT [directory]

```bash
	django-admin startproject drinks .
```

## run server

```bash
	python manage.py runserver
```
