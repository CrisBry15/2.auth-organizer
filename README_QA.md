This microservice registers organizers and validates their credentials using their ID 
and personal token to ensure they're real.

A Flask-based authentication microservice for organizer management with JWT token authentication.

## Technologies

- **Backend Framework**: Flask 3.1.1
- **Database**: MySQL with mysql-connector-python
- **Authentication**: JWT (JSON Web Tokens) with Flask-JWT-Extended
- **Password Hashing**: bcrypt
- **CORS**: Flask-CORS for cross-origin requests
- **Containerization**: Docker

## Architecture & Design Patterns

- **Microservice Architecture**: Standalone authentication service
- **MVC Pattern**: Controller-based logic separation
- **Blueprint Pattern**: Flask blueprints for route organization
- **Repository Pattern**: Direct database access in controllers
- **Factory Pattern**: App factory in `init.py`

## API Endpoints

- `GET /organizer/` - Health check
- `POST /organizer/register` - Organizer registration
- `POST /organizer/login` - Organizer authentication
- `GET /organizer/protected` - Protected route (requires JWT)

## Communication Protocols

- **HTTP/HTTPS**: RESTful API endpoints
- **JSON**: Request/response data format
- **Bearer Token**: JWT authentication in Authorization header