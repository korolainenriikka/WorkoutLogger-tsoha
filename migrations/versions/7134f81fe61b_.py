"""empty message

Revision ID: 7134f81fe61b
Revises: 45a127d5e37d
Create Date: 2020-03-30 11:53:25.462168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7134f81fe61b'
down_revision = '45a127d5e37d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('account_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'result', 'account', ['account_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'result', type_='foreignkey')
    op.drop_column('result', 'account_id')
    # ### end Alembic commands ###
