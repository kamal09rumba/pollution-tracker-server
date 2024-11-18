# Pollurion Tracker Server

Repository for Pollution Tracker Server

## Table of Contents
- [Requirement](#requirement)
- [Install](#install)


## Requirement
  - Git
  - [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
  - Python 3.10+
  - Flask 3.1.0+
  - PostgreSQL 13+

## Install
### Clone the repositary
```bash
git clone --branch develop https://github.com/kamal09rumba/pollution-tracker-server.git && cd pollution-tracker-server
```
### Setup using docker-compose 

1. Create external-service docker network `docker network create external-services`
2. Soft link `docker/docker-compose.yml`
3. Create `.env` file from `.env.example` and set appropriate and required environmental variable as explained in `.env.example`
4. Run command `ln -s docker/external_services.yml external-services.yml` and  `docker-compose -f external-services.yml up -d`
    - To create database run command `docker exec postgis13 psql -U postgres -c 'create database DATABASE_NAME;'.`. Replace DATABASE_NAME with actual database
5. Run `docker-compose up -d` to start server
6. Access server using url http://localhost:5555

### Post-installation
1. Run command `poetry run python app/seed.py` to generate sample historical pollution data