"""initial

Revision ID: 1d011f22eef8
Revises: 3e57d09a7422
Create Date: 2024-02-21 18:32:30.004896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d011f22eef8'
down_revision: Union[str, None] = '3e57d09a7422'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
