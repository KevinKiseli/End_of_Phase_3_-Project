"""initial

Revision ID: f491fd6e527b
Revises: 271a3849ed3b
Create Date: 2024-02-19 20:20:11.721270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f491fd6e527b'
down_revision: Union[str, None] = '271a3849ed3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
