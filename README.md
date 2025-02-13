# **Car Sales API**

## Overview

#### Car Sales API is a FastAPI-based backend service that allows users to manage car listings and user authentication with JWT.

## Features

- User registration and authentication (JWT)

- CRUD operations for cars

- PostgreSQL database integration

- Dockerized setup

## Installation

#### Prerequisites

- Docker & Docker Compose installed

#### Steps

1. git clone git@github.com:Alkan0/CarSales_FastAPI.git
    
    cd CarSales_FastAPI
2. docker-compose up 

## API Endpoints

#### Authentication
- POST /auth/login → Login and receive JWT

- POST /auth/register → Register a new user

#### Users
- GET /users/ → Get all users (Requires authentication)
- GET /users/{user_id} → Get user by ID

#### Cars
- GET /cars/ → Get all cars
- POST /cars/ → Add a new car (Requires authentication)
- GET /cars/{car_id} → Get a car by ID
- PUT /cars/{car_id} → Update a car (Requires authentication)
- DELETE /cars/{car_id} → Delete a car (Requires authentication)

## Testing
You can test the API using Postman or directly via the interactive Swagger UI:
- Open http://localhost:8000/docs after running the server.

Feel free to clone.