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

Each entity and mapping is implemented in a separate Django app.

## Features

- Modular Django project structure
- CRUD APIs using APIView
- Foreign key mapping between entities
- Unique constraint validation
- Admin panel support
- Swagger API documentation
- ReDoc documentation

## Project Setup

Clone the repository:
