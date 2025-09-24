# UniManage

Sistema de gestión de inventarios universitarios.

## About

UniManage is a web application to manage university assets, including loans and maintenance.

## Features

-   **Asset Management**: Create, read, update, and delete assets.
-   **Loan Management**: Manage asset loans to users.
-   **Maintenance Management**: Track asset maintenance.
-   **Reporting**: View dashboards with asset statistics.
-   **User Authentication**: User registration and login.

## Technologies

-   **Backend**: Django, Python
-   **Frontend**: HTML, Tailwind CSS, JavaScript
-   **Database**: MySQL

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/user/unimanage.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure the database in `unimanage/settings.py`.
4.  Run the migrations:
    ```bash
    python manage.py migrate
    ```
5.  Start the development server:
    ```bash
    python manage.py runserver
    ```
