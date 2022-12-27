"""empty message

Revision ID: 6f1e471a1935
Revises: 0d83f8b97f52
Create Date: 2022-12-26 17:56:27.346765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f1e471a1935'
down_revision = '0d83f8b97f52'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
