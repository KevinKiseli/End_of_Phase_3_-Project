"""initial

Revision ID: bd770b6420c8
Revises: a1de28cadd30
Create Date: 2024-02-18 21:38:41.910238

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd770b6420c8'
down_revision: Union[str, None] = 'a1de28cadd30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
