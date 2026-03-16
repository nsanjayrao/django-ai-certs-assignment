# Django Modular Entity and Mapping System

This project implements a modular Django REST Framework backend using APIView only.

## Tech Stack
- Python
- Django
- Django REST Framework
- drf-yasg (Swagger Documentation)

## Master Entities
- Vendor
- Product
- Course
- Certification

## Mapping Entities
- Vendor → Product
- Product → Course
- Course → Certification

## Features
- Modular Django apps
- CRUD APIs using APIView
- Foreign key mapping between entities
- Duplicate mapping prevention
- Swagger API documentation
- ReDoc documentation
- Admin panel support

## Project Setup

Clone the repository

git clone https://github.com/nsanjayrao/django-ai-certs-assignment.git

Go to project folder

cd django-ai-certs-assignment

Create virtual environment

python -m venv venv

Activate environment

Windows:
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py makemigrations
python manage.py migrate

Run server

python manage.py runserver

## API Documentation

Swagger
http://127.0.0.1:8000/swagger/

ReDoc
http://127.0.0.1:8000/redoc/

## Admin Panel

http://127.0.0.1:8000/admin

Create superuser

python manage.py createsuperuser
