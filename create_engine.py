from sqlalchemy import create_engine
from config import settings

table_uri = settings.get_postgres_url()
engine = create_engine(table_uri)

engine.connect()