This guest book built using:
- Python 3.11
- Django 4.1.5
- built in database sqlite3


How to run:

1. Clone this repo

2. Open cmd and go to the file directory (example C:Downloads/guest-book-using-django4.1)

3. Create virtual environment -> python -m venv Env

4. Go to the virtual environment directory and type -> Env\Scripts\activate.bat

5. Once entered virtual environtment, install django -> pip install django==4.1.5
   You can check if it's already installed or not by type -> pip list
   If you noticed to upgrade pip, just follow and type -> python.exe -m pip install --upgrade pip

6. Enter the guesbook_base directory (example C:Downloads/guest-book-using-django4.1/guestbook_base)

7. Create database migrations -> python manage.py make migrations

8. Migrate the database -> python manage.py migrate

9. Run the server -> python manage.py runserver 

10. Type in browser -> http://127.0.0.1:8000/show
    **note:it's empty in the database, so you have to add new guest before operating CRUD
    Now you can CRUD(create, read, update, delete) the guestbook

11. To stop the server -> CTRL+C in cmd 

11. To exit virtual environment, stop the server first and type type -> deactivate
