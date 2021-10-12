# Six-Hats
Six-Hats Application

## Setup
1. Clone the project
   > git clone https://github.com/endrajadhage/Six-Hats.git
2. Install virtulenv (https://pypi.python.org/pypi/virtualenv)
3. Create and activate virtualenv
   > python3 -m venv env <br/>
   > source env/bin/activate
5. Setup database
   > cd sixhats <br/>
   > python manage.py makemigrations
   > python manage.py migrate
6. Run the server
   > python manage.py runserver
7. Check if application is running correctly
   > http://127.0.0.1:8000/
8. Create superuser for the admin backend
   > python manage.py createsuperuser
9. Login as superuser
   > http://127.0.0.1:8000/admin
10. To get all user list use follow api
    http://127.0.0.1:8000/user/
    for piganation change page size in setting.py file
    PAGESIZE=3
11. To edit ,delete use follow api
    http://127.0.0.1:8000/userdetails/2/
