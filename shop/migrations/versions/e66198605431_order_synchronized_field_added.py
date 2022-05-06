"""Order.synchronized field added

Revision ID: e66198605431
Revises: 8f90f66eaca4
Create Date: 2022-05-04 11:38:53.023026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e66198605431'
down_revision = '8f90f66eaca4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('synchronized', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'synchronized')
    # ### end Alembic commands ###