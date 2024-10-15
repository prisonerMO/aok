#!/bin/bash

rm -f db.sqlite3

rm -f communities/migrations/0*.py
rm -f events/migrations/0*.py
rm -f news/migrations/0*.py

echo ""
echo ""
python manage.py makemigrations


echo ""
echo ""
python manage.py migrate


echo ""
echo ""
python manage.py createsuperuser
