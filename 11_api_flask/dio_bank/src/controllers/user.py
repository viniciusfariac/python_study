from flask import Blueprint, request
from src.app import db, User
from http import HTTPStatus
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Blueprint("user", __name__, url_prefix="/users")

def _create_user():
    data = request.json
    user = User(
        username=data["username"], 
        password=data["password"], 
        role_id=data["role"])
    db.session.add(user)
    db.session.commit()


def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [ {
        "id": user.id,
        "username": user.username,
        "role": {
            "name": user.role.name,
            "id": user.role.id
        }
    } 
    for user in users ]

@app.route("/", methods=["GET", "POST"])
@jwt_required()
def handle_user():

    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)

    if (user.role.name != "admin"):
        return {"message": "Forbidden, you dont have acess."}, HTTPStatus.FORBIDDEN

    if request.method == "POST":
        _create_user()
        return {
            'message': 'User created!',
        }, HTTPStatus.CREATED
    else:
        return _list_users()
    

@app.route("/<int:user_id>")
@jwt_required()
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id,
        "name": user.username
    }


@app.route("/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    # Apenas um elemento
    # if "username" in data:
    #     user.username = data["username"]
    #     db.session.commit()

    # Mais de um atributo para modificar
    # attrs = ["adrress", "userName", "FirstName"]
    # for attr in attrs:
    #     setattr(user, attr, data[attr])
    # db.session.commit

    # mais de um atributo dinâmico
    mapper = inspect(User)

    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    db.session.commit()

    return {
        "id": user.id,
        "username": user.username,
    }

@app.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT