# Address Book FastAPI

## Features

- Create, Update, Delete Address
- SQLite database
- Geolocation-based filtering using geopy
- Input validation using Pydantic
- Logging enabled

## API Endpoints

POST /addresses  
GET /addresses  
PUT /addresses/{id}  
DELETE /addresses/{id}  
GET /addresses/nearby?lat=&lon=&distance=

## Setup

Clone repo

git clone https://github.com/shivangitripathi2225/fastapi-geolocation-address-book.git

cd address-book-fastapi

## Create virtual environment

python -m venv venv

source venv/bin/activate

## Install dependencies

pip install -r requirements.txt

## Run server

uvicorn app.main:app --reload

## Swagger

http://127.0.0.1:8000/docs
