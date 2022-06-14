# Django URLs
This project demonstrates usage of urls.py (within project folder level) boilerplate for creating admin user and modifying url path to admin login interface.

## To Create Admin User
Creating Admin user, do the following:
python manage.py migrate
python manage.py createsuperuser

Supply your desire username, email (optional), password, confirm password and press Enter

## To Start Server
Run this command: python manage.py runserver
Through the local domain: http://127.0.0.1:8000/admin/ or http://localhost:8000/admin
Supply your login credentials and login

## To Modify the local domain endpoint from 'admin' -> 'zuri-admin'
Within project directory (i.e directory that contains manage.py and project setup directory (actually the same name as project_directory name)), locate urls.py file. And change the path from admin to zuri-admin. NOTE: Don't the quote around path as string value.