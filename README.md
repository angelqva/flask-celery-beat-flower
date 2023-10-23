# FLASK CELERY BEAT FLOWER

## How to Execute

-   Requeriments: ***docker***, ***docker-compose***
-   RUN: `cd /path/to/project`
-   RUN: `cp .env.local .env`
-   RUN: `docker-compose up -d --build`

## Content

-   `http://127.0.0.1:5555/` ***Flower logger of tasks***
-   `http://127.0.0.1:5000/api/` ***ejecutara la tarea sync_task***
-   `http://127.0.0.1:5000/api/beers` ***method:Get -> list beers***
-   `http://127.0.0.1:5000/api/beers` ***method:Post -> create beers***
-   `http://127.0.0.1:5000/api/beers/<string:id>` ***method:Put -> update beers***
-   `http://127.0.0.1:5000/api/beers/<string:id>` ***method:Delete -> delete beers***
-   `http://127.0.0.1:5000/api/beers/<string:id>` ***method:Get -> retrieve beers***


## Tasks

-   ***periodic***: example of periodic task with beat
-   ***sync_task***: example of async task with celery