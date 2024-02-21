# movie_ratings/migrate.py


from alembic import command
from alembic.config import Config

alembic_cfg = Config("alembic.ini")

def run_migrations():
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_migrations()

