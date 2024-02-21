# alembic/versions/002_create_tables.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'movie_details',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('movie_id', sa.Integer(), sa.ForeignKey('movies.id'), nullable=False),
        sa.Column('director', sa.String(100)),
        sa.Column('release_date', sa.DateTime()),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('movie_details')
