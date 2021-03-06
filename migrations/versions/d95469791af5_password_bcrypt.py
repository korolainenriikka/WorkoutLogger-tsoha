"""password bcrypt

Revision ID: d95469791af5
Revises: 747c9d6e1c6d
Create Date: 2020-03-26 14:50:12.835603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95469791af5'
down_revision = '747c9d6e1c6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('password_hash', sa.String(length=144), nullable=False))
    op.drop_column('account', 'password')
    op.drop_column('result', 'rndTesti')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('rndTesti', sa.VARCHAR(length=144), nullable=True))
    op.add_column('account', sa.Column('password', sa.VARCHAR(length=144), nullable=False))
    op.drop_column('account', 'password_hash')
    # ### end Alembic commands ###
