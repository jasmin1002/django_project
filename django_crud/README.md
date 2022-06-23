# Introduction to Class Base View in Django

## Django CRUD
This project shows practical approach in setting up blog app for CRUD operation in Django.\
CRUD stands for **Create**, **Read/Retrieve**, **Update**, and **Delete**. Basic operations for **Request - Response** through server to database.


## Views
This project also demonstrates practical use of Class Base View, cbv. This is so for the following reasons:
* Code Reusability (i.e through inheritance)
* Dry principle: **Don't Repeat Yourself** principle

The following are example of Class Base View:
* ListView
* CreateView
* UpdateView
* DetailView
* FormView
* TemplateView etc

## Templates
Template makes it possible to return full html document along sent back response. Django various\
template engine like jinja2, Genshi but this project uses jinja2. Template engine gives purview of
* template tag
* dynamic url
* passing and retrieving values to template etc

## Environment Variable
This project uses Django-environ for abstracting the variable variables like:
* SECRET_KEY
* DEBUG
* database setup