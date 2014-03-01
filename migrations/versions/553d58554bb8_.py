"""empty message

Revision ID: 553d58554bb8
Revises: 2433567e4c07
Create Date: 2014-03-01 17:20:21.409398

"""

# revision identifiers, used by Alembic.
revision = '553d58554bb8'
down_revision = '2433567e4c07'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('discription', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column(u'articles', sa.Column('category_name', sa.String(length=10), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'articles', 'category_name')
    op.drop_table('category')
    ### end Alembic commands ###