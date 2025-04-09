import os
import subprocess

def run_command(command):
    subprocess.run(command, shell=True, check=True)

# Create Django project
run_command('django-admin startproject personal_blog .')

# Create main app
run_command('python manage.py startapp main')

# Create templates directory
os.makedirs('templates/main', exist_ok=True)
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)
os.makedirs('static/images', exist_ok=True)

print("Project structure created successfully!") 