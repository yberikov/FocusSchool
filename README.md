# FocusSchool - Automated Teacher Training Reporting System


## Overview

FocusSchool is a Python Django project developed to automate the teacher training reporting process for a local school. This web application provides an efficient and user-friendly platform for teachers and administrators to manage training reports, eliminating the need for paper-based reporting.

## Features

- **Online Reporting Forms**: SchoolFocus offers online forms for teachers to submit training reports. This digitization simplifies the reporting process and reduces paperwork.

- **Digital Report Viewing**: Teachers and administrators can conveniently view training reports in a digital format, making it easier to access and manage the data.

- **Examiner and Auditee Roles**: The application includes roles for examiners and auditees, allowing for quick and effective interaction between users involved in the training process.

## Getting Started

### Prerequisites

Before running FocusSchool, make sure you have the following prerequisites installed:

- Python 3.x
- Django
- <add any other dependencies here>

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yberikov/FocusSchool.git
  

2.  Change to the project directory:
    ```bash
    cd FocusSchool
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply database migrations:
    ```bash
    python manage.py migrate
5. Create a superuser account (admin):
    ```bash
    python manage.py createsuperuser
6.Start the development server:
```bash
python manage.py runserver
