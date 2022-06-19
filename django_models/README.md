# Django Models
This project demonstrates practical and general steps involve in creating models for applications in django projects. Django Models is class blueprint for a table in a database. Every model in django project represent table in django database

## To Create an app in Django Project
* python manage.py startapp <app_name>\
Note: Make sure you are in directory that houses 'manage.py' file before running the command.

## To Create a model in Django Project
* Change directory to app directory
* Import model from django.db
* Inherit from models.Model
* Create necessary fields according to project model requirements

## Running Migrations
* Ensure app is registered in setting.py under INSTALLED_APPS
* python manage.py makemigrations to update the database for new model to reflect
* python manage.py migrate

## Environment Variables
I used django-environ package to manage some SECRET credentials

## Outside Project Scope Boundary
I created some functions within a views.py to handle some url request endpoint\
Just for testing purpose for the new created model (i.e Post). I used Templates\
To accomplish this purpose.