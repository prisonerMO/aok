@echo off

del db.sqlite3

del communities\migrations\0*.py
del events\migrations\0*.py
del news\migrations\0*.py

echo.
echo.
python manage.py makemigrations


echo.
echo.
python manage.py migrate


echo.
echo.
python manage.py createsuperuser