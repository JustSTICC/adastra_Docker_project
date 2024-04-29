
from flask_sqlalchemy import SQLAlchemy
from modules import GraphicsEngine
from flask import request


def create_engine(db: SQLAlchemy):
    new_engine = GraphicsEngine(
        name=request.form["name"],
        language=request.form["language"],
    )
    db.session.add(new_engine)
    db.session.commit()
