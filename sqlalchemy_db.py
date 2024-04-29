from modules import Base
from flask_sqlalchemy import SQLAlchemy
from create_engine import engine

db = SQLAlchemy(model_class=Base)
Base.metadata.create_all(engine)

