# studentidrett-backend

# Running locally

## Install Docker
https://docs.docker.com/get-docker/

## Create .env file
For the system to run corretly it requires a set of environment variables:

```
# Django
DJANGO_SECRET_KEY= [INSERT_KEY]

# Postgres
POSTGRES_DB=[DATABASE_NAME]
POSTGRES_USER=[DATABASE_USERNAME]
POSTGRES_PASSWORD=[DATABASE_PASSWORD]
POSTGRES_HOST=postgres
```
## Run Docker Machine
Make sure to have a Docker Daemon running to be able to run the project.
This can be done by running `docker-machine start default` and `
@FOR /f "tokens=*" %i IN ('docker-machine env') DO @%i`. Find the ip-address that Docker-machine
runs on by running `docker-machine ip`. This will be the access point to test
the project, and is by default `192.168.99.100`.

## Run the project
To run the project locally, simply run `docker-compose -f docker-compose.local.yml up --build -d`
at the root of the project. This will install dependencies and run migrations and create a docker image
with the app running.

### Dependencies

Dependencies are stored in `requirements.txt`, and is installed by running `pip install -r requirements.txt`.

After adding a new dependency, run `pip freeze > requirements.txt` to update.

# Git-conventions

Automatic linting, code formatting and security testing is implemented using
[pre-commit](https://pre-commit.com/), with isort, Black, Flake8 and Bandit.
To enable run `pre-commit install` once, and then `pre-commit autoupdate`.

The pre-commit hooks will then run before every commit, and check the files changed.
To run on all files, run `pre-commit run --all-files`

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