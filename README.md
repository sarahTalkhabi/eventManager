# eventManager
Event Manager App

This is a REST API for an event manager app built with Django and Django Rest Framework. It allows users to create a personal account, log in, create, edit, fetch, and register to attend events. Each event has at least a name, a description, a start date and end date, and a list of attendees.
Features

    User registration and login: Users can create an account and log in to the app.
    Token-based authentication: The API uses token-based authentication with access and refresh tokens. The access token is valid for 1 hour and the refresh token is valid for 1 day.
    Event creation and editing: Users can create new events and edit events they have created.
    Event retrieval: Users can retrieve a list of all events or a list of events they have created.
    Event registration: Users can register to attend events or unregister from events that have not yet started.

Setup

To set up the project, follow these steps:

    Clone the repository to your local machine.
    Create a virtual environment and activate it.
    Apply the database migrations by running python manage.py migrate.
    Start the server by running python manage.py runserver.

Usage
API Endpoints

    /api/user/register/ (POST): User registration
    /api/user/login/ (POST): User login and token generation
    /api/user/refresh/ (POST): Token refresh
    /api/validate/ (GET): Token validation
    /api/events/ (GET, POST): Event listing and creation
    /api/events/<event_id>/ (GET, PUT): Event details and editing
    /api/attendance/<event_id>/register/ (POST): Event registration
    /api/attendance/<event_id>/unregister/ (POST): Event un-registration/
