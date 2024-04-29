from typing import Tuple
from flask_sqlalchemy import SQLAlchemy
from modules import Game, Developer, GraphicsEngine
from sqlalchemy import select
from flask import request


def update_game(db: SQLAlchemy):

    game_id = request.form["id"]
    game_to_update = db.get_or_404(Game, game_id)
    game_to_update.title = request.form["title"]
    game_to_update.developer_id = request.form["developer"]
    game_to_update.graphics_engine_id = request.form["engine"]
    game_to_update.price = request.form["price"]
    db.session.commit()


def get_update_data(db: SQLAlchemy) -> Tuple:

    game_id = request.args.get('id')
    game_selected = db.get_or_404(Game, game_id)
    developers = db.session.execute(select(Developer.id, Developer.name))
    engines = db.session.execute(select(GraphicsEngine.id, GraphicsEngine.name))
    return game_selected, developers, engines
