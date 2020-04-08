"""empty message

Revision ID: 6b351bdd2a99
Revises: f78b566e22cc
Create Date: 2020-04-08 11:18:55.807041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b351bdd2a99'
down_revision = 'f78b566e22cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conditioning', 'workout')
    op.drop_column('result', 'description')
    op.alter_column('session', 'account_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('session', 'date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('session', 'date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('session', 'account_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('result', sa.Column('description', sa.VARCHAR(length=144), nullable=True))
    op.add_column('conditioning', sa.Column('workout', sa.VARCHAR(), nullable=False))
    # ### end Alembic commands ###