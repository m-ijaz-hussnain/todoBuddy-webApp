
# ✅ TodoBuddy

**TodoBuddy** is a simple yet powerful task management web app built with **Django**.  
It helps you manage daily tasks and projects efficiently — add, edit, and track your todos with ease.

---

## 🌟 Features

✨ **Add, Edit, and Delete Tasks** — Manage your tasks effortlessly.  
✅ **Mark Tasks as Complete or Incomplete** — Stay on top of your goals.  
🔍 **View Task Details** — Access important task info in one click.  
🎨 **User-Friendly Interface** — Clean, responsive, and easy to use.  

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django (Python) |
| Database | SQLite / PostgreSQL |
| Frontend | HTML / CSS / JavaScript / Django Templates |
| Styling | Bootstrap / Tailwind CSS |
| Authentication | Django Auth System |
| Deployment | Render / Railway / PythonAnywhere / Heroku |

---

## 🚀 Getting Started

Follow these steps to set up **TodoBuddy** locally:

### 1. Clone the Repository
```bash
git clone https://github.com/m-ijaz-hussnain/todoBuddy.git
cd todoBuddy
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Then open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser 🚀

---

## 💡 Usage

1. Create an account or log in via Django’s authentication system.
2. Add new tasks — set title, description, and status.
3. Edit or delete tasks anytime.
4. Track your progress easily through the dashboard.

---

## 🧩 Folder Structure

```
TodoBuddy/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── todo_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── todoBuddy/   # Project settings folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── db.sqlite3
```

---

## 📸 Screenshots

![Home Screenshot](assets/home.png)
![TaskList Screenshot](assets/task_list.png)

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork the repo
2. Create a new branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes

   ```bash
   git commit -m "Added new feature"
   ```
4. Push and open a Pull Request

---

## 🛡️ License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

📧 **Author:** Muhammad Ijaz Hussnain
🔗 **GitHub:** [@m-ijaz-hussnain](https://github.com/m-ijaz-hussnain)
🌐 **Project Link:** [https://github.com/m-ijaz-hussnain/todoBuddy](https://github.com/m-ijaz-hussnain/todoBuddy)

---
Would you like me to also create a **sample `requirements.txt`** file for this Django project (with Django, crispy forms, etc.) so you can include it before uploading to GitHub?
```
