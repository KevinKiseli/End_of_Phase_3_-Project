"""initial

Revision ID: 3e57d09a7422
Revises: ec9858083686
Create Date: 2024-02-21 18:32:15.316059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e57d09a7422'
down_revision: Union[str, None] = 'ec9858083686'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
