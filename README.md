# FastAPI Address Book API

A minimal Address Book API built with FastAPI that allows users to create, update, delete, and retrieve addresses. The API also supports geolocation-based filtering to find addresses within a given distance from provided coordinates.

## Features

- Create, update, delete, and list addresses
- Store address coordinates (latitude, longitude)
- SQLite database integration
- SQLAlchemy ORM usage
- Input validation with Pydantic
- Geolocation-based nearby address search using geopy
- Logging for API operations and failures
- Environment-based configuration using `.env`

## Project Structure

address-book-fastapi/
│
├── app/
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── loggers.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/shivangitripathi2225/fastapi-geolocation-address-book
cd fastapi-address-book-api
```

## Create virtual environment

## Mac/Linux 
```bash
python -m venv venv
source venv/bin/activate
```

## Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file in project root:

```env
DATABASE_URL=sqlite:///./address.db
```

## Run the application
```bash
uvicorn app.main:app --reload
```

## Swagger API Docs
## Once the server is running, open:
http://127.0.0.1:8000/docs

## API Endpoints
- POST /addresses → Create address
- GET /addresses → List all addresses
- GET /addresses/nearby?lat=&lon=&distance= → Find nearby addresses
- PUT /addresses/{address_id} → Update address
- DELETE /addresses/{address_id} → Delete address

## Example Request Body
```json
{
  "name": "Home",
  "street": "Connaught Place",
  "city": "Delhi",
  "latitude": 28.6139,
  "longitude": 77.2090
}
