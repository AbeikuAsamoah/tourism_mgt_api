# TOURISM API
A Django REST Framework API for managing tours and bookings.
The system allows tourists to register, browse tours and create bookings

## Features
- Custom user model with roles (Tourist / Admin)
- User registration and authentication
- Browse or view available tours
- Create bookings
- Token-based authentication
- RESTful API endpoints

## Tech Stack
- Python
- Django
- Django REST Framework
- Token Authentication
- SQLite

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependences
4. Run migrations
5. Run the server

## Authentication
The API uses Token Authentication

## API Endpoints

### Users
- Register User
POST /api/users/register/

- User Login
POST /api/users/login/

### Tours
- List All Tours
GET api/tours/

- Retrieve Tour Details
GET /api/tours/<id>/

- Create Tour
POST /api/tours/create/

- Update Tour
PATCH /api/tours/update/<id>/

- Delete Tour
DELETE /api/tours/delete/<id>/

### Bookings
- List Bookings
GET /api/bookings/

- Create Bookings 
POST /api/bookings/create/

- Cancel Bookings
DELETE /api/bookings/cancel/<id>/

## Example Workflow
1. Register a user
2. Login and obtain authentication token
3. View available tours
4. Create a booking
5. View or cancel bookings

## Deployment
The API was deployed using PythonAnywhere

## Author
Collins Abeiku Asamoah
