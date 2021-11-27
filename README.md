Set up
```
git clone https://github.com/sohyunp3/to-do-list-and-calendar.git
cd to-do-list-and-calendar

virtualenv env
source env/bin/activate
pip3 install django

python3 manage.py migrate
python3 manage.py runserver
```
Find the app running at http://localhost:8000/calendar/
