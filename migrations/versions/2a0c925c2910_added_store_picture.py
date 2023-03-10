"""added store picture

Revision ID: 2a0c925c2910
Revises: 21faf73123e5
Create Date: 2023-01-05 14:52:53.023309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a0c925c2910'
down_revision = '21faf73123e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('store_bild', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stores', schema=None) as batch_op:
        batch_op.drop_column('store_bild')

    # ### end Alembic commands ###
