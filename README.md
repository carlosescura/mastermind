# Mastermind game
Mastermind game via REST API done with Django and Django REST Framework.

# Prerequisites
- Python 3.6 with a new virtual environment (for local testing and development)
- [Docker](https://docs.docker.com/docker-for-mac/install/) (optional)
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/) (optional)


# Environment variables setup

| VARIABLE NAME  | DEFAULT VALUE | NEEDED IN PRODUCTION | NEEDED IN LOCAL  | ACCEPTED VALUES |
|----------------|---------------|----------------------|------------------|-----------------|
|DJANGO_SECRET_KEY|(in config file)|YES|YES|string|
|DJANGO_CONFIGURATION|Local|YES|YES|Local, Production, Test|
|DJANGO_SETTINGS_MODULE|mastermind.config|YES|YES|n/a|
|DATABASE_NAME|postgres|YES|YES|string|
|DATABASE_USER|postgres|YES|YES|string|
|DATABASE_PASSWORD||YES|YES|string|
|DATABASE_HOST|db|YES|YES|string|
|DJANGO_AWS_ACCESS_KEY_ID||YES|NO|string|
|DJANGO_AWS_SECRET_ACCESS_KEY| |YES|NO|string|
|DJANGO_AWS_STORAGE_BUCKET_NAME| |YES|NO|string|


# Local Development

## Using python and python virtualenv

Install project dependencies:
```bash
pip install -r requirements
```

Migrate database:
```bash
python manage.py migrate
```

Create a test admin user:
```bash
python manage.py createsuperuser --username my_user_name
```

Start the development server:
```bash
python manage.py runserver
```



## Using docker and docker-compose

Start the dev server for local development:
```bash
docker-compose up -d
```

To run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

Therefore, to create the first admin user in Djanjo console:

```bash
docker-compose run --rm web bash

$ python manage.py createsuperuser --username my_user_name
```




# Continuous Deployment

Deployment can be automated via Travis, CircleCI, Jenkins, etc.

Note that production servers (or service provider) must have all the required ENV_VARS configured for a successful deployment
and ``DJANGO_CONFIGURATION`` should be ``Production``


# Usage

## Main models
This app includes two main models: Game and Guess.

First, a remote user requests the creation of a game, by providing a name via a
POST message to `/api/v1/games/` :
```
{
    "name": "Your Game Name"
}
```

The user can also retrieve the list of created games via a
GET request to `/api/v1/games/`

After a game is created, it will contain a randomly generated code of four colours, being the possible
choices one of:

* RED
* BLUE
* GREEN
* YELLOW

Next step is try to solve the game with a
POST message to `/api/v1/guess/`:
```
{
    "guess_code": ["RED","BLUE","GREEN","YELLOW"],
    "game": 1
}
```

Being the game number, the game ID

After successfully posting a new guess, the response will return the created guess as well as
the obtained score for it.

The score is returned in a format of a list of individual scores, being 1 a full match of both color and position
and 0 a partial match of color but not position.

You can request the complete list of guesses and its score for a given game using the endpoint `/api/v1/games/{gameID}`


# TODO:
* Add user attribute to each game and guess and provide private game views
