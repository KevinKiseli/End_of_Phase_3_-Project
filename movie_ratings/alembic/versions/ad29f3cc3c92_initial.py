"""initial

Revision ID: ad29f3cc3c92
Revises: 5cce750ef61c
Create Date: 2024-02-20 18:48:58.869373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad29f3cc3c92'
down_revision: Union[str, None] = '5cce750ef61c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
