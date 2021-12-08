"""users added

Revision ID: 04ceb25828fd
Revises: 6a47da610b5e
Create Date: 2021-12-07 17:25:33.486430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04ceb25828fd'
down_revision = '6a47da610b5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('role', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_foreign_key(None, 'addresses', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'addresses', type_='foreignkey')
    op.drop_table('users')
    # ### end Alembic commands ###