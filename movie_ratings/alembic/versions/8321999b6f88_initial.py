"""initial

Revision ID: 8321999b6f88
Revises: b2a19785b9c6
Create Date: 2024-02-18 20:32:01.299310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8321999b6f88'
down_revision: Union[str, None] = 'b2a19785b9c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
