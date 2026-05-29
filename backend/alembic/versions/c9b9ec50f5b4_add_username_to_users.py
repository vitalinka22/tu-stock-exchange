"""add username to users

Revision ID: c9b9ec50f5b4
Revises: 5468d9510b3b
Create Date: 2026-05-29 21:22:36.691264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9b9ec50f5b4'
down_revision: Union[str, None] = '5468d9510b3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'username')
