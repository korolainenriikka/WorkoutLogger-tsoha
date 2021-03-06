"""empty message

Revision ID: 0fbd45f3c24c
Revises: 8b408b4eebb3
Create Date: 2020-04-18 22:01:38.026400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fbd45f3c24c'
down_revision = '8b408b4eebb3'
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
    op.drop_table('user_usergroup')
    op.drop_table('userUsergroup')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userUsergroup',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('usergroup_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['usergroup_id'], ['usergroup.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'usergroup_id')
    )
    op.create_table('user_usergroup',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('usergroup_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['usergroup_id'], ['usergroup.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('UserUsergroup')
    # ### end Alembic commands ###
