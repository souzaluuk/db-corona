from sys import argv
from settings import engine
from models import Base


def create_migrate(engine_local=None):
    Base.metadata.create_all(engine_local or engine)


def drop_migrate(engine_local=None):
    Base.metadata.drop_all(engine_local or engine)


if __name__ == "__main__":
    if len(argv) > 0:
        if argv[1] == 'createmigrate':
            create_migrate()
        elif argv[1] == 'dropmigrate':
            drop_migrate()
        else:
            print('Argumento desconhecido')
    else:
        print('Nenhuma opção informada')
