"""initial

Revision ID: 9b2ab7c0e5c3
Revises: 3823b1814b27
Create Date: 2024-02-21 10:44:38.172432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b2ab7c0e5c3'
down_revision: Union[str, None] = '3823b1814b27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
