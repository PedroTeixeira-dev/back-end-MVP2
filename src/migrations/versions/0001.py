"""empty message

Revision ID: 0001
Revises: 
Create Date: 2024-06-19 18:30:44.398683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('custumers',
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('cep', sa.String(length=8), nullable=True),
    sa.Column('uf', sa.String(length=10), nullable=True),
    sa.Column('city', sa.String(length=30), nullable=True),
    sa.Column('street', sa.String(length=40), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('complement', sa.String(length=100), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('custumers')
    # ### end Alembic commands ###
