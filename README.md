To start using these scripts, you need to:
- Have Python installed
- Have Postgresql installed
- Download this repository to your local machine
- Create a new postgresql database and add all necessary information to ```.env.local```
- Create a virtual environment using the command ```python -m venv .venv```
- Activate the virtual environment: ```.venv\Scripts\activate```
- Install all necessary dependencies: ```pip install -r requirements.txt```
- Then you can run it ```python app.py``` and go to ```http://localhost:8000/devices```

## Run in docker container
- add all necessary information to .env
- Build ```docker-compose build```
- run ```docker compose up```

## Tests
- Be able to use a new (clean) database to run tests (tests create new items in db), so you need to use a new database
- Run tests locally
- run ```pytest ```
