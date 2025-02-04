# Number Classification API
## Overview
This FastAPI-based microservice provides detailed mathematical classifications for input numbers.
## Features
- Determine prime numbers
- Identify Armstrong numbers
- Calculate digit sum
- Retrieve mathematical fun facts
- Full CORS support
## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
3. Activate the virtual environment:
    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## Running the API
Start the API server:
```sh
uvicorn main:app --reload
```
## Endpoint
GET /api/classify-number?number=371
## Response Example
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number"
}
```
## Technologies
- FastAPI
- Python
- Requests Library
- Numbers API
## Deployment
Can be deployed on platforms like Heroku, Railway, or DigitalOcean