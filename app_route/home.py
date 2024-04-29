from typing import Tuple
from flask_sqlalchemy import SQLAlchemy
from modules import Game, Developer
from sqlalchemy import select, Engine
import pandas


def get_home(engine: Engine, db: SQLAlchemy) -> Tuple:

    df = pandas.read_sql(select(Game.title, Developer.name).join_from(Game,Developer), engine)
    games_by_developers = df.groupby('name')['title'].count()
    games = db.session.query(Game).all()
    developers = db.session.query(Developer.id, Developer.name).all()

    return games_by_developers, games, developers
