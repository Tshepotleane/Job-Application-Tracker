# Job Application Tracker

A web-based Job Application Tracker built with Python and Flask. The application helps users keep track of job applications, update application information, manage application statuses, and remove applications when they are no longer needed.

## Features

- Add new job applications
- View all saved applications
- Edit existing applications
- Update application status
- Delete applications
- Store application data using SQLite
- Simple and clean web interface

## Application Status

The tracker supports the following application statuses:

- Applied
- Interview
- Rejected
- Accepted

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2
- Git
- GitHub

## Project Structure

job-application-tracker/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css

## How It Works

The application uses Flask as the backend framework and SQLite as the database.

Users can add a job application by entering:

- Company
- Job Position
- Date Applied
- Application Status

Saved applications are displayed in a table. Each application can be edited or deleted using the available action buttons.

The Edit feature allows users to update existing application information without creating a new record.

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL