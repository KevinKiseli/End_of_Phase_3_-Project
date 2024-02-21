"""initial

Revision ID: 40801f9479ca
Revises: d24f85fd9ca7
Create Date: 2024-02-20 18:24:38.284561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40801f9479ca'
down_revision: Union[str, None] = 'd24f85fd9ca7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
