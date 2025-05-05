# Django ToDo App 📝

A simple task management application built with **Django** and styled using **Bootstrap 5**.

This app supports:
- User registration, login and logout
- Creating, editing, and deleting tasks (CRUD)
- Filtering tasks by status (done / not done)
- Authenticated user ownership (each user sees only their tasks)
- Clean Bootstrap-styled interface

---

## 🚀 Features

- 🧑‍💻 Authentication (login, logout, signup)
- 📋 Task CRUD (create, read, update, delete)
- 🔍 Task filtering (all / done / not done)
- 🧼 Clean UI with Bootstrap 5
- 🔐 Per-user access (your tasks only)

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- Bootstrap 5 (via CDN)
- SQLite (or PostgreSQL if configured)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/django-todo.git
cd django-todo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # or just: pip install django

# Run migrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
