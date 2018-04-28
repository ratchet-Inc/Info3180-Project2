"""empty message

Revision ID: 98496ae8d2fe
Revises: 
Create Date: 2018-04-28 06:28:24.443094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98496ae8d2fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follow',
    sa.Column('f_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('f_id')
    )
    op.create_table('likes',
    sa.Column('l_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('l_id')
    )
    op.create_table('posts',
    sa.Column('p_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(length=64), nullable=True),
    sa.Column('capt', sa.String(length=128), nullable=True),
    sa.Column('created', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('p_id')
    )
    op.create_table('user_profile',
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('fname', sa.String(length=32), nullable=True),
    sa.Column('lname', sa.String(length=32), nullable=True),
    sa.Column('passcode', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('loc', sa.String(length=64), nullable=True),
    sa.Column('bio', sa.String(length=128), nullable=True),
    sa.Column('profImg', sa.String(length=64), nullable=True),
    sa.Column('joined', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('u_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    op.drop_table('posts')
    op.drop_table('likes')
    op.drop_table('follow')
    # ### end Alembic commands ###
