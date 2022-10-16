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

## Make Migrations

I've done a little bit of code for home page GET, but now need to do some migrations
how? like this:

```bash
	python manage.py migrate
```

```bash
	python manage.py makemigrations
```

## Need to add things to settings.py

add the app we created "drinks" and "rest_framework" to the installed apps

```python
	INSTALLED_APPS = [
		...
		'drinks',
		'rest_framework',
		...
	]
```

# Connect from app to the DB in AWS

## Using the tool Boto3

```bash
	pip3 install boto3
```

## Create simple table in DynamoDB in AWS

go to AWS and search for "DynamoDB" and click on "create table"
Table Name: drinks
Partition Key: name (string)
table config: custom (so avoid any charges in my credit card haha)
(AWS does not charge for read and write, it charges for the speed this uses)
limit Read to 5 units
limit Wite to 5 or 1 unit
create table
go to create new element
example:
name: grape soda (string)
description: very grapey (string)
