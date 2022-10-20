#Commerce site for bidding 

A website that allows users to:
* Create listings for their products
* Add products in their watchlist
* Bid on products
* Make comments on the products.

The users can **Register**, **Login** and **Logout** from the site. The website is implementing Django for the backend, and it utilizes Django Templates for the frontend.


# Build process
1. You should create a virtual environment in which you will install Django
```
pip install Django

```
2. Create an sqlite3 Database
```
python manage.py migrate

```
3. Run the application locally
```
python manage.py runserver

```
To view the application, enter to you browser's url input 
```
127.0.0.1:8000
```
the local adress on which the application runs on. 

# Extra
You can create an admin user account that gives you the admin interface, a very useful tool that allows you to manipulate your application's data in an intuitive way.

To create such an account you need to write the command
```
python manage.py createsuperuser

```
fill in the inputs and you have successfuly created an admin account!

To access the admin interface while running the application locally, type in the browser url page
```
127.0.0.1:8000
```
fill in the credentials you added previously and that's it.


