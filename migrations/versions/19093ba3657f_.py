"""empty message

Revision ID: 19093ba3657f
Revises: c79240f1fe94
Create Date: 2020-04-01 13:04:43.510385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19093ba3657f'
down_revision = 'c79240f1fe94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'result', 'session', ['session_id'], ['id'])
    op.drop_column('result', 'date')
    op.drop_column('result', 'rndTesti')
    op.drop_column('result', 'date_modified')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('date_modified', sa.DATETIME(), nullable=True))
    op.add_column('result', sa.Column('rndTesti', sa.VARCHAR(length=144), nullable=True))
    op.add_column('result', sa.Column('date', sa.DATETIME(), nullable=True))
    op.drop_constraint(None, 'result', type_='foreignkey')
    # ### end Alembic commands ###
