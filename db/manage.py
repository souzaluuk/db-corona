from sys import argv


def make_migrate():
    from settings import engine
    from models import Base
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    if len(argv) > 0:
        if argv[1] == 'migrate':
            make_migrate()
    else:
        print('Nenhuma opção informada')
