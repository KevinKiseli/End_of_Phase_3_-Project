"""initial

Revision ID: d24f85fd9ca7
Revises: f491fd6e527b
Create Date: 2024-02-19 20:28:44.008529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd24f85fd9ca7'
down_revision: Union[str, None] = 'f491fd6e527b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
