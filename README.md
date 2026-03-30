Student Manager (Django Project)

📌 Project Overview

This is a simple Django-based web application that allows users to manage student records.
The project provides basic CRUD functionality (Create, Read, Update, Delete) using standard Django views (no Django REST Framework).

Users can:

* Add new students
* View the student list
* Edit student details
* Delete student records

⚙️ Technologies Used

* Python
* Django
* HTML / CSS
* SQLite (default Django database)

🚀 Features

* Student registration form
* Login & Signup system
* View all students
* Edit student information
* Delete student records
* Success page after submission

🔗 URL Routes

The following URL patterns are defined in the project:

* `/admin/` → Admin panel
* `/` → Add student form
* `/signup/` → User signup
* `/login/` → User login
* `/logout/` → User logout
* `/success/` → Student submission success page
* `/list/` → View all students
* `/edit/<str:student_id>/` → Edit student
* `/delete/<int:student_id>/` → Delete student

❗ Error Note

If you see this error:


The current path didn’t match any of these.
It means the URL you entered in the browser does not match any defined route in `urls.py`.
For example:
* Invalid URL: `/j`
* Correct URL: `/`, `/list/`, `/login/`, etc.

🛠️ Installation & Setup

1. Clone the repository:

```
git clone <your-repo-link>
```

2. Navigate to project folder:

```
cd student_manager
```

3. Create virtual environment:

```
python -m venv venv
```

4. Activate virtual environment:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Apply migrations:

```
python manage.py migrate
```

7. Run the server:

```
python manage.py runserver
```

8. Open in browser:

```
http://127.0.0.1:8000/
```


📂 Project Structure (Basic)

```
student_manager/
│
├── student_manager/
│   ├── urls.py
│   ├── settings.py
│
├── student/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│
├── manage.py
```

📄 License

This project is for learning purposes and can be used freely.


👨‍💻 Author

Ronak Raja (Ronak Lodha)
