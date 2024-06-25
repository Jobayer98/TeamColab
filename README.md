## Project Title

### TeamColab Management System

## Description

A comprehensive project management system to manage users, projects, tasks, and comments efficiently. This system allows users to register, login, create and manage projects and tasks, and collaborate through comments.

## Technologies

- Python
- Django
- Django REST Framework
- SQLite (default)
- JWT (for authentication)

## Features

- User authentication (registration and login)
- CRUD operations for users, projects, tasks, and comments
- JWT-based authentication
- RESTful API endpoints

## Project Setup

### Setup with `venv`

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jobayer98/TeamColab.git
   cd TeamColab
   ```

2. **Create a virtual environment:**
   ```bash
    python -m venv env
   ```
3. **Activate the virtual environment:**
   - On Windows:
   ```bash
    .\env\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
    source env/bin/activate
   ```
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply migrations to setup the database:**
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser (optional but recommended for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the server:**
   ```bash
   python manage.py runserver
   ```
8. **Access the application:** <br>
   Open your web browser and go to` http://127.0.0.1:8000/` or ` http://127.0.0.1:8000/swagger-doc/`

## API Routes and Endpoints

## API Endpoints

| Feature  | HTTP Method | Endpoint                          | Description                               |
| -------- | ----------- | --------------------------------- | ----------------------------------------- |
| Refresh  | POST        | api/token/refresh/                | Return access token                       |
|          |             |                                   |                                           |
| Docs     | GET         | swagger-doc/                      | Swagger Documentation                     |
|          |             |                                   |                                           |
| Users    | POST        | /api/users/register/              | Create a new user                         |
|          | POST        | /api/users/login/                 | Authenticate a user and return a token    |
|          | GET         | /api/users/{id}/                  | Retrieve details of a specific user       |
|          | PUT/PATCH   | /api/users/{id}/                  | Update user details                       |
|          | DELETE      | /api/users/{id}/                  | Delete a user account                     |
| Projects | GET         | /api/projects/                    | Retrieve a list of all projects           |
|          | POST        | /api/projects/                    | Create a new project                      |
|          | GET         | /api/projects/{id}/               | Retrieve details of a specific project    |
|          | PUT/PATCH   | /api/projects/{id}/               | Update project details                    |
|          | DELETE      | /api/projects/{id}/               | Delete a project                          |
| Tasks    | GET         | /api/projects/{project_id}/tasks/ | Retrieve a list of all tasks in a project |
|          | POST        | /api/projects/{project_id}/tasks/ | Create a new task in a project            |
|          | GET         | /api/tasks/{id}/                  | Retrieve details of a specific task       |
|          | PUT/PATCH   | /api/tasks/{id}/                  | Update task details                       |
|          | DELETE      | /api/tasks/{id}/                  | Delete a task                             |
| Comments | GET         | /api/tasks/{task_id}/comments/    | Retrieve a list of all comments on a task |
|          | POST        | /api/tasks/{task_id}/comments/    | Create a new comment on a task            |
|          | GET         | /api/comments/{id}/               | Retrieve details of a specific comment    |
|          | PUT/PATCH   | /api/comments/{id}/               | Update comment details                    |
|          | DELETE      | /api/comments/{id}/               | Delete a comment                          |
