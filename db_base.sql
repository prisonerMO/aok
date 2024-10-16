
-- Removing everything
--DROP SCHEMA IF EXISTS aok;
--DROP SCHEMA IF EXISTS django;
DROP DATABASE IF EXISTS aok;
DROP ROLE IF EXISTS svc_aok;
DROP ROLE IF EXISTS svc_django;

-- Creating roles and database
CREATE ROLE svc_aok WITH LOGIN PASSWORD 'aokpwd';
CREATE ROLE svc_django WITH LOGIN PASSWORD 'djangopwd';
CREATE DATABASE aok OWNER svc_aok;
\connect aok;

-- Creating Django schema and permissions for Django user
CREATE SCHEMA IF NOT EXISTS django AUTHORIZATION svc_django;
GRANT ALL ON SCHEMA django TO svc_django;

-- Creating App schema and permissions for App role
CREATE SCHEMA IF NOT EXISTS aok AUTHORIZATION svc_aok;
GRANT ALL ON SCHEMA aok TO svc_aok;

