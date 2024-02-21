"""initial

Revision ID: 3823b1814b27
Revises: ad29f3cc3c92
Create Date: 2024-02-20 20:25:37.090790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3823b1814b27'
down_revision: Union[str, None] = 'ad29f3cc3c92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
