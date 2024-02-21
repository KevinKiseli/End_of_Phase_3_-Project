"""initial

Revision ID: 271a3849ed3b
Revises: bd770b6420c8
Create Date: 2024-02-18 21:40:59.876928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '271a3849ed3b'
down_revision: Union[str, None] = 'bd770b6420c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
