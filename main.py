from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math
import requests
app = FastAPI()
# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def is_armstrong_number(n):
    # Ensure we're working with positive numbers
    if n < 0:
        return False
    num_str = str(abs(n))
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == abs(n)
def is_perfect_number(n):
    if n <= 0:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)
@app.get("/api/classify-number")
async def classify_number(number: str):
    try:
        num = int(number)
    except ValueError:
        return {
            "number": number,
            "error": True
        }
    # Properties determination
    properties = []
    if is_armstrong_number(num):
        properties.append("armstrong")
    properties.append("even" if num % 2 == 0 else "odd")
    # Get number fact
    try:
        fact = requests.get(f"http://numbersapi.com/{abs(num)}/math", timeout=5).text
    except:
        fact = "No fact available"
    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect_number(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": fact
    }
@app.get("/")
async def root():
    return {"message": "Number Classification API is running"}