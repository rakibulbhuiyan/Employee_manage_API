# Employer Management System

## Setup Instructions

1. Clone the repo
2. Create a virtual environment and activate it

## API Endpoints

### Auth
- POST `/api/auth/signup/` -> Register
- POST `/api/auth/login/` -> Get JWT
- GET `/api/auth/profile/` -> Get current user

### Employers
- POST `/api/employers/` -> Create Employer
- GET `/api/employers/` -> List Employers
- GET `/api/employers/<id>/` -> Retrieve
- PUT `/api/employers/<id>/` -> Update
- DELETE `/api/employers/<id>/` -> Delete
