import uuid
from flask import jsonify
from settings import constants
from beers.models import Beer

db = constants.db


def create_beer(data: dict):
    id = str(uuid.uuid4())
    beer: Beer = Beer(id=id, name=data['name'], style=data['style'])
    status = 400
    try:
        db.session.add(beer)
        db.session.commit()
        newBeer: Beer = Beer.query.get(id)
        response = newBeer.toDict()
        status = 201
    except:
        response = {'message': 'check your data'}
        status = 400
    return jsonify(response), status


def list_beers():
    beers: list[Beer] = Beer.query.all()
    response = [beer.toDict() for beer in beers]
    return jsonify(response), 200


def retrieve_beer(id: int):
    beer: Beer = Beer.query.get(id)
    response = {'message': 'Beer not found'}
    status = 404
    if beer is not None:
        status = 200
        response = beer.toDict()
    return jsonify(response), status


def update_beer(id: int, data: dict):
    beer: Beer = Beer.query.get(id)
    response = {'message': 'Beer not found'}
    status = 404
    if beer is not None:
        status = 200
        if data.get("name"):
            beer.name = data['name']
        if data.get("style"):
            beer.style = data['style']
        try:
            db.session.commit()
            response = beer.toDict()
        except:
            response = {'message': 'check your data'}
            status = 400
    return jsonify(response), status


def destroy_beer(id: int):
    beer: Beer = Beer.query.get(id)
    response = {'message': 'Beer not found'}
    status = 404
    if beer is not None:
        db.session.delete(beer)
        db.session.commit()
        response = {'message': 'Beer deleted successfully'}
    return jsonify(response), status


def send_task(task_name="", message=""):
    response = {'message': f'Task {task_name}: schedule success'}
    status = 202
    if len(message) > 0:
        response = {'message': f'Task {task_name}: {message}'}
        status = 400
    return jsonify(response), status
