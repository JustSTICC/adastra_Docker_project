from flask_sqlalchemy import SQLAlchemy
from modules import Developer
from flask import request


def create_dev(db: SQLAlchemy):

    new_dev = Developer(
        name=request.form["name"],
        address=request.form["address"],
    )
    db.session.add(new_dev)
    db.session.commit()
