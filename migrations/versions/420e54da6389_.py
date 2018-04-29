"""empty message

Revision ID: 420e54da6389
Revises: 98496ae8d2fe
Create Date: 2018-04-29 20:11:38.324147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '420e54da6389'
down_revision = '98496ae8d2fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('f_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('f_id')
    )
    op.drop_table('follow')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follow',
    sa.Column('f_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('f_id', name=u'follow_pkey')
    )
    op.drop_table('follows')
    # ### end Alembic commands ###
