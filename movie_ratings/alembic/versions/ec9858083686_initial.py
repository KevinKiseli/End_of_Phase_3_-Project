"""initial

Revision ID: ec9858083686
Revises: 3a965eedf26d
Create Date: 2024-02-21 18:23:40.020862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec9858083686'
down_revision: Union[str, None] = '3a965eedf26d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
