"""empty message

Revision ID: b8c00e6c4696
Revises: 1c10ad5f283d
Create Date: 2020-04-14 10:37:38.355248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c00e6c4696'
down_revision = '1c10ad5f283d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'conditioning', 'session', ['workout_id'], ['id'])
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
    op.drop_constraint(None, 'conditioning', type_='foreignkey')
    # ### end Alembic commands ###