from flask import request
from modules import Game
from flask_sqlalchemy import SQLAlchemy


def delete_game(db: SQLAlchemy):

    game_id = request.args.get('id')
    game_to_delete = db.get_or_404(Game, game_id)
    db.session.delete(game_to_delete)
    db.session.commit()
