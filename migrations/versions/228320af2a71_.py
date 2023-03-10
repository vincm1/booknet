"""empty message

Revision ID: 228320af2a71
Revises: 973d6b3cb6df
Create Date: 2022-12-18 15:51:25.792403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228320af2a71'
down_revision = '973d6b3cb6df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('passwort_hash', sa.String(), nullable=False))
        batch_op.drop_column('passwort')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('passwort', sa.VARCHAR(length=15), autoincrement=False, nullable=False))
        batch_op.drop_column('passwort_hash')

    # ### end Alembic commands ###
