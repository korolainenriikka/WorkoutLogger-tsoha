"""empty message

Revision ID: 5863ec0e4bc4
Revises: 3f32799fd6f8
Create Date: 2020-04-29 16:09:37.570392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5863ec0e4bc4'
down_revision = '3f32799fd6f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserUsergroup',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('usergroup_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['usergroup_id'], ['usergroup.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'usergroup_id')
    )
    op.drop_table('userUsergroup')
    op.add_column('conditioning', sa.Column('distance', sa.Integer(), nullable=False))
    op.add_column('conditioning', sa.Column('time', sa.Time(), nullable=False))
    op.drop_column('result', 'time')
    op.drop_column('result', 'distance')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('distance', sa.INTEGER(), nullable=False))
    op.add_column('result', sa.Column('time', sa.TIME(), nullable=False))
    op.drop_column('conditioning', 'time')
    op.drop_column('conditioning', 'distance')
    op.create_table('userUsergroup',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('usergroup_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['usergroup_id'], ['usergroup.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'usergroup_id')
    )
    op.drop_table('UserUsergroup')
    # ### end Alembic commands ###
