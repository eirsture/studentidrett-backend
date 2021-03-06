# studentidrett-backend

## Description
This project is the back end for The Norwegian Association of University Sports' (Norges Studentidrettsforbund, NSI) website
that is meant to let students find NSI's sports offers all over Norway. There is also a questionnaire that recommends
sports based on the answers given. Admins can use the back end to create new objects in the database, as well as a
primitive view of interests (clicks) on groups from the front end.

Back end is hosted at: https://kundestyrt-nsi-backend.azurewebsites.net/ \
Swagger for back end: https://app.swaggerhub.com/apis/kundestyrt_h20/Backend/v3

Front end is hosted at: https://kundestyrt-nsi-frontend-staging.azurewebsites.net/ \
Front end repository: https://github.com/Studentidrettsforbundet/studentidrett-frontend


## Technologies
This is a general overview of the technologies used in the project.
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Elasticsearch](https://www.elastic.co/elasticsearch/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Azure](https://azure.microsoft.com/)

### Dependencies

Dependencies are stored in `requirements.txt`, and is installed automatically by Docker and can be manually installed by running `pip install -r requirements.txt`.

After adding a new dependency to the project, add it to `requirements.txt` in the proper subsection, or create a new fitting subsection. \
Running `pip freeze > requirements.txt` to update the dependency list will add many unnecessary packages and dependencies of dependencies, and should not be used.

## Installation and running locally
Running the project locally can be done using either Docker or running it as a normal Python and Django project. \
The installation guide assumes [Python 3](https://www.python.org/downloads/) has already been installed and that the repository has been cloned.

### Create .env file
The .env file should be created inside the first `app` directory
For the system to run correctly it requires a set of environment variables:

```
# General
ENV_NAME= ['local' (default), 'staging', 'production'] (Not needed for running locally)

# Django
DJANGO_SECRET_KEY= [INSERT_KEY] (Not needed for running locally)

# Postgres
POSTGRES_DB=[DATABASE_NAME]
POSTGRES_USER=[DATABASE_USERNAME]
POSTGRES_PASSWORD=[DATABASE_PASSWORD]
POSTGRES_HOST=[DATABASE_HOST, 'localhost' (default)]

# Elasticsearch
ELASTICSEARCH=[ELASTICSEARCH_HOST, 'localhost:9200' (default)]
```

### Option 1 - Using Docker
#### Install and run Docker
https://docs.docker.com/get-docker/


#### Install and run Docker Machine
If you have an older Mac or Windows system you will need to install and use Docker Machine, since you cannot enable
 Hyper-V services. If your system supports Hyper-V services you can skip this part.

Installation guide for Docker Machine can be found at:
https://docs.docker.com/machine/install-machine/

After installation do the following:

Make sure to have a Docker Daemon running to be able to run the project.
This can be done by running `docker-machine start default` and `
@FOR /f "tokens=*" %i IN ('docker-machine env') DO @%i`. Find the ip-address that Docker-machine
runs on by running `docker-machine ip`. This will be the access point to test
the project, and is by default `192.168.99.100`.

#### Run the project
To run the project locally, simply run `docker-compose -f docker-compose.local.yml up --build -d`
at the root of the project. This will install dependencies and run migrations and create a docker image
with the app running.

The project should now be accessible from [localhost:8000](http://localhost:8000/)


### Option 2 - Running as a Python file
#### Environmental variables
```
POSTGRES_HOST
ELASTICSEARCH
```
These environmental variables use the default values and will have to be changed if the setup is done in a different way.

#### Set up virtual environment
To create a virtual environment run: \
`python -m venv .venv` \
This will create a virtual environment named `.venv` in the root directory.

Activation of the virtual environment depends on the operating system.

**POSIX (Linux, macOS, \*BSD, etc.):** \
`source .venv/bin/activate`

**Windows:** \
`.venv\Scripts\activate.bat`

#### Install dependencies
Navigate to directory containing `requirements.txt`: \
`cd app`

Install dependencies: \
`pip install -r requirements.txt`

#### Install and run Elasticsearch
https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html

#### Install PostgreSQL
https://www.postgresql.org/download/

#### Create PostgreSQL database
https://www.guru99.com/postgresql-create-database.html

Make sure that all variables coincide with what is stored in the `.env` file.

#### Migrate database
Run migrations so the PostgreSQL database have all tables and columns needed for the project. \
`python manage.py migrate`

#### Run the project
Run project as an ordinary Python project, using the runserver command. \
`python manage.py runserver`

The project should now be accessible from [localhost:8000](http://localhost:8000/)

## Testing
Running the tests requires Elasticsearch to be running either through Docker or [manually running](https://github.com/Studentidrettsforbundet/studentidrett-backend/tree/fix/readme#install-and-run-elasticsearch).

To run the tests you need to be in the `./app` folder and run the command: \
`pytest --cov`

## Other notable commands
These commands might be necessary when developing or debugging.

If you have changed anything with search or want to clear the search cache: \
`python manage.py search_index --rebuild`

To shut down the Docker containers: \
`docker-compose -f docker-compose.local.yml down -v`

To remove all Docker images: \
`docker image prune -a`

## Code style
Automatic linting, code formatting and security testing is implemented using
[pre-commit](https://pre-commit.com/), with isort, Black, Flake8 and Bandit.
To enable run `pre-commit install` once, and then `pre-commit autoupdate`.

The pre-commit hooks will then run before every commit, and check the files changed.
To run on all files, run `pre-commit run --all-files`

When the pre-commit hooks automatically run and any of them fail, the attempted committed files need to be re-added and committed again.

*More about code standards can be found in the [GitHub wiki](https://github.com/Studentidrettsforbundet/studentidrett-backend/wiki/Code-Standards)*

## Git-conventions

Branches:

- main: update only for deployment (merge from dev)
- dev: development branch, update continuously
- feat/feature-name: a branch that creates/improves a new feature into dev
- task/task-name: a branch that creates/improves a new task into feat. Is used when multiple developers work on a feature
- design/area-name: a branch that creates/improves GUI/UX into dev
- fix/bug-name: a branch that fix a bug or security issue for dev

Pull requests:

- At least one collaborator have to review and approve a pull request before it is merged into dev-branch
- Always use "Squash and merge" as merge-options

