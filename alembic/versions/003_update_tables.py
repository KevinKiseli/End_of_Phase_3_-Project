# alembic/versions/003_update_tables.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add new tables
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('genres', sa.String(200), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'users_table',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'movie_details',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('movie_id', sa.Integer(), sa.ForeignKey('movies.id'), nullable=False),
        sa.Column('director', sa.String(100)),
        sa.Column('release_date', sa.DateTime()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'ratings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(50), sa.ForeignKey('users_table.username'), nullable=False),
        sa.Column('movie_id', sa.Integer(), sa.ForeignKey('movies.id'), nullable=False),
        sa.Column('ratings', sa.Float(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Drop new tables
    op.drop_table('ratings')
    op.drop_table('movie_details')
    op.drop_table('users_table')
    op.drop_table('movies')
