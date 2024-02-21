# alembic/versions/001_create_database.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.execute("CREATE DATABASE IF NOT EXISTS movie_ratings.db")

def downgrade():
    op.execute("DROP DATABASE IF EXISTS movie_ratings.db")
