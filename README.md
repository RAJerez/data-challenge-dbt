# Data Challenge - DBT

This project focuses on data processing for the data-challenge, this time applying DBT models.

Data will be consumed from 3 tables with raw information about Argentine libraries, museums and cinemas in a Postgres database.

## Data processing
Data processing will allow our project to transform the data of the
source files in the information that will feed the database. For this, the
project must:

- Normalize all the information from museums, cinemas and libraries and generate tables that have the following columns.
    - cod_localidad
    - id_provincia
    - id_departamento
    - categoría
    - provincia
    - localidad
    - nombre
    - domicilio
    - código postal
    - número de teléfono
    - mail
    - web

- Process the joint data to generate a table with the following information:
    - Cantidad de registros totales por categoría
    - Cantidad de registros totales por fuente
    - Cantidad de registros por provincia y categoría


- Process the cinema information to create a table that contains:
    - Provincia
    - Cantidad de pantallas
    - Cantidad de butacas
    - Cantidad de espacios INCAA


## Pre requirements

- python==3.10
- docker==25.0.12
- dbt-postgres==1.7.4
- poetry==1.7.1

#### Poetry
I used Poetry 1.7.1 for better dependency management and also to create my virtual environment.

Install poetry from pipx and the installation will be carried out isolated from the global environment
    
    pipx install poetry==1.7.1

To install the necessary dependencies described in pyproyect.toml

    poetry install

A virtual environment will automatically be created that you can access

    poetry shell


#### Option without Poetry
If you do not use poetry you can install the dependencies through requirements.txt
The project was carried out with Python 3.10

    python3 -m virtualenv venv

    source venv/bin/activate

    pip install -r 'requirements.txt'


## Creation of database, tables and pipeline execution
I build a container with Postgres Database:

    sudo docker compose up -d

You can access the database from bash:

    docker exec -it postgres psql -U postgres -d data-challenge-dbt

Loading raw data into database
The following script connects to the database and loads.

    python3 main.py

Run dbt models:

    dbt run
