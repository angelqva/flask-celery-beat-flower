from flask import request, Blueprint
from beers.controllers import create_beer, retrieve_beer, update_beer, destroy_beer, list_beers, send_task
from .tasks import sync_task


beers_router = Blueprint("beers_router", __name__)

@beers_router.route('/')
def hello():
    return "Hello World!!"

@beers_router.route('/api')
def sample():
    task_name = "sync_task"
    message = ""
    try:
        sync_task.delay()
    except Exception as e:
        message = repr(e)
    return send_task(task_name=task_name, message=message)


@beers_router.route("/api/beers", methods=['GET', 'POST'])
def list_create_beers():
    if request.method == 'GET':
        return list_beers()
    if request.method == 'POST':
        data = request.get_json()
        return create_beer(data=data)


@beers_router.route("/api/beers/<string:id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_beers(id):
    if request.method == 'GET':
        return retrieve_beer(id=id)
    if request.method == 'PUT':
        data = request.get_json()
        return update_beer(id=id, data=data)
    if request.method == 'DELETE':
        return destroy_beer(id)
    else:
        return 'Method is Not Allowed'
