"""initial

Revision ID: a1de28cadd30
Revises: 8321999b6f88
Create Date: 2024-02-18 20:33:53.237163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1de28cadd30'
down_revision: Union[str, None] = '8321999b6f88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
