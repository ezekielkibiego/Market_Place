"""update product migration

Revision ID: dff2f78ceca1
Revises: 7f3aa18aa281
Create Date: 2024-02-11 05:30:00.681078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dff2f78ceca1'
down_revision = '7f3aa18aa281'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['owner'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('owner')

    # ### end Alembic commands ###
