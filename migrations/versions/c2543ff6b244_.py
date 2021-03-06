"""empty message

Revision ID: c2543ff6b244
Revises: 7134f81fe61b
Create Date: 2020-03-30 11:57:05.667616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2543ff6b244'
down_revision = '7134f81fe61b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('account_id', sa.Integer(), nullable=False, default=0))
    op.create_foreign_key(None, 'result', 'account', ['account_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'result', type_='foreignkey')
    op.drop_column('result', 'account_id')
    # ### end Alembic commands ###
