Event Tracker Platform
    A simplified event tracking platform with REST APIs and background task processing using Celery.

Technologies Used
Django (Backend framework)

Django REST Framework (API creation)

Celery (Background task processing)

Redis (Broker for Celery)

SQLite (Database for simplicity)

Docker (Containerization)


Local Development Setup

    Clone the Repository:
        git clone <repo-url>
        cd event_tracker

Install Dependencies:
    pip install -r requirements.txt

Apply Migrations:

    python manage.py migrate

Run the Django Server:
    python manage.py runserver


Docker Setup

    Build the Docker Containers:
        docker-compose build
        docker-compose up -d


Environment Variables (.env)

    CELERY_BROKER_URL=redis://redis:6379/0
    SQLITE_DB_PATH=./db.sqlite3


API Endpoints
    POST /api/events/: Create a new event.
    
        Request Body:
            {
                "type": "event_type",
                "source": "event_source",
                "timestamp": "2025-05-07T00:00:00Z"
            }
            
        
        Response:
        
            {
                "id": 1,
                "type": "event_type",
                "source": "event_source",
                "timestamp": "2025-05-07T00:00:00Z"
            }

GET /api/events/: List all events.

    Response:
        {
            "count": 7,
            "next": "http://localhost:8003/api/events/?page=2",
            "previous": null,
            "results": [
            {
            
                    "id": 1,
                    "type": "login",
                    "source": "web",
                    "timestamp": "2025-05-07T12:00:00Z"
                  }
            ]
            }



GET /api/events/<id>/: Get a specific event.

    Response:
        {
            "id": 1,
            "type": "event_type",
            "source": "event_source",
            "timestamp": "2025-05-07T00:00:00Z"
        }


Notes
SQLite is used in this project for simplicity and to save time. While PostgreSQL would be more suitable for a production-level application, SQLite is a lightweight, file-based database that requires minimal setup, making it ideal for quick assessments and development.

Redis is used for Celery’s task processing.

Docker is used to containerize the application, ensuring a consistent environment.
