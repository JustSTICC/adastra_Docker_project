from typing import Tuple
from flask_sqlalchemy import SQLAlchemy
from modules import Game, Developer, GraphicsEngine
from sqlalchemy import select
from flask import request


def create_game(db: SQLAlchemy):

    new_game = Game(
        title=request.form["title"],
        developer_id=request.form["developer"],
        graphics_engine_id=request.form["engine"],
        price=request.form["price"]
    )
    db.session.add(new_game)
    db.session.commit()


def get_options(db:SQLAlchemy) -> Tuple:
    developers = db.session.execute(select(Developer.id, Developer.name))
    engines = db.session.execute(select(GraphicsEngine.id, GraphicsEngine.name))
    return developers, engines
