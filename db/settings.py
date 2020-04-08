from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from environs import Env

env = Env()
env.read_env()

name = env('POSTGRES_DB')
user = env('POSTGRES_USER')
password = env('POSTGRES_PASSWORD')
host = env('POSTGRES_HOST', 'localhost')
port = env('POSTGRES_PORT', '5432')

engine = create_engine(
    f'postgresql://{user}:{password}@{host}:{port}/{name}')

Session = sessionmaker(bind=engine)
