# MyProject
# 📝 To-Do List App (Django)

A simple but professional **To-Do List web application** built with **Django**.  
This app lets users **create, edit, delete, and mark tasks as complete**, with priorities, due dates, and a clean Bootstrap-based UI.  

---

## 🚀 Features
- ✅ Add, edit, and delete tasks  
- 🔄 Mark tasks as complete or pending  
- 🎯 Set priorities (Low, Medium, High)  
- 📅 Add optional due dates  
- 🔍 Filter tasks (All, Completed, Pending)  
- 🎨 Responsive UI with **Bootstrap 5**  
- ⚡ Flash messages for user feedback  

---

## 📂 Project Structure
todolist/ # Main Django project
│
├── tasks/ # Django app for tasks
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates
│ │ └── tasks/
│ │ ├── task_list.html
│ │ └── task_form.html
│ ├── admin.py # Register models for admin site
│ ├── apps.py
│ ├── forms.py # Task form
│ ├── models.py # Task model
│ ├── views.py # Views (CRUD logic)
│ └── urls.py # App-specific URLs
│
├── todolist/ # Project settings
│ ├── settings.py # Installed apps, DB setup
│ ├── urls.py # Main URL routes
│ ├── asgi.py
│ └── wsgi.py
│
├── manage.py # Django CLI
├── requirements.txt # Project dependencies
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/Mikol-0519/to_do_list
cd todolist

python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

🛠️ Technologies Used

Python 3

Django

SQLite3 (default DB, can be swapped with PostgreSQL/MySQL)

Bootstrap 5

📌 Future Improvements

🔑 User authentication (login/signup with personal task lists)

📱 Better mobile support

🌙 Dark mode