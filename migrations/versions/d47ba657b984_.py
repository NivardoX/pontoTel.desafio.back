"""empty message

Revision ID: d47ba657b984
Revises: 306e75e0f0c4
Create Date: 2020-10-27 10:42:46.693694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd47ba657b984'
down_revision = '306e75e0f0c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quotes', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'quotes', 'companies', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quotes', type_='foreignkey')
    op.drop_column('quotes', 'company_id')
    # ### end Alembic commands ###
