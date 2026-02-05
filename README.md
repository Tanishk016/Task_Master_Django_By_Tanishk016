# 📝 Task Master
### *Stop forgetting things. Start getting things done.*

**Task Master** is a robust, secure, and professional To-Do application built with **Django**. It helps users organize their daily life with a clean interface, secure login system, and smart task management features.

---

## ✨ Key Features

* **🔐 Secure Authentication:**
    * Sign Up & Log In system.
    * Users can only see and edit *their own* tasks.
    * Secure logout protection.
* **✅ Full CRUD Functionality:**
    * **Create** new tasks instantly.
    * **Read** your list in a clean dashboard.
    * **Update** tasks (edit typos or change details).
    * **Delete** tasks you no longer need.
* **🎨 Modern UI/UX:**
    * Professional "Card" layout for forms.
    * **Material Design Icons** for a sleek look.
    * **SweetAlert2** integration for animated deletion popups.
    * Responsive design that looks good on any screen.
* **⚡ Smart Interactions:**
    * Toggle tasks as "Completed" with a single click.
    * Safety checks before deleting important data.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Django 5+
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite (Built-in)
* **Design:** Custom CSS + Material Icons
* **Libraries:** SweetAlert2 (for popups)

---

## 🚀 How to Run this Project

Follow these steps to get the project running on your local machine.

### 1. Prerequisites
Make sure you have **Python** and **Git** installed on your computer.

### 2. Clone the Repository
Open your terminal/command prompt and run:
```bash
git clone [https://github.com/YOUR_USERNAME/task-master-django.git](https://github.com/YOUR_USERNAME/task-master-django.git)
cd task-master-django
```


### 3. Create a Virtual Environment
It is best practice to keep dependencies isolated so they don't mess up your system.

Bash**
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate



### 4. Install Dependencies
This project requires Django. You can install it manually or from the requirements file.

Option A: Install from list (Recommended)

Bash
```
pip install -r requirements.txt
```
Option B: Manual Install

Bash
```
pip install django
```



### 5. Set Up the Database
Create the necessary database tables (migrations).

Bash
```
python manage.py migrate
```



### 6. Create a Superuser (Optional)
If you want to access the Admin Panel:

Bash
```
python manage.py createsuperuser
```



### 7. Run the Server
Start the application!

Bash
```
python manage.py runserver
```



### 8. Access the App
Open your browser and visit: 👇
```
 https://www.google.com/search?q=http://127.0.0.1:8000

```





-----------------------------------------------------------------------------------

# 👤 Author 
## Designed & Developed by Tanishk Built with ❤️ using Django 

-----------------------------------------------------------------------------------
