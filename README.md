### Clone repository

```bash
$ git clone https://github.com/souzaluuk/db-corona/
$ cd db-corona
```

### Install virtual environment

```bash
$ python3 -m venv env
$ source env/bin/activate
(env)$ pip install -r requeriments.txt
```

### Create db/.env file
```bash
(env)$ cp db/.env.example db/.env
```

### Create production db

```bash
(env)$ docker-compose up -d postgres
(env)$ python db/manage.py createmigrate # to create schema in db
(env)$ python db/manage.py dropmigrate # to drop schema in db
```

### Run tests

```bash
(env)$ docker-compose up -d db-tests
(env)$ cd db
(env)$ python -m unittest -v
```

### Run example

```bash
(env)$ docker-compose [up|start] postgres
(env)$ python example.py
```
