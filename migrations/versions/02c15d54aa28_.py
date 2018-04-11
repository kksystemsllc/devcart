"""empty message

Revision ID: 02c15d54aa28
Revises: 4427deb9f71c
Create Date: 2018-04-10 21:25:41.187536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02c15d54aa28'
down_revision = '4427deb9f71c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('inventory', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'admin')
    op.drop_table('product')
    # ### end Alembic commands ###
