#!/bin/bash

#rm -f db.sqlite3

rm -f communities/migrations/0*.py
rm -f events/migrations/0*.py
rm -f news/migrations/0*.py

cp db_base.sql /tmp/
sudo su - postgres -c "psql -f /tmp/db_base.sql"
