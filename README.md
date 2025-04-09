# Personal Blog Website

A Django-based personal blog website showcasing professional information, education, skills, and work experience.

## Features

- Professional profile display
- Education history
- Work experience
- Skills showcase
- Project portfolio
- Contact information

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the website. 