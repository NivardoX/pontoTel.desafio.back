"""empty message

Revision ID: b38fe4612cee
Revises: 75d184616165
Create Date: 2020-10-27 00:07:38.016437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38fe4612cee'
down_revision = '75d184616165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('symbol', sa.String(length=255), nullable=False),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('symbol')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companies')
    # ### end Alembic commands ###
