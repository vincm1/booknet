"""Buchregal model angelegt

Revision ID: eaf75b3020fc
Revises: 517c2f2715f3
Create Date: 2022-12-28 15:39:00.656249

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eaf75b3020fc'
down_revision = '517c2f2715f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buchregale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('flask_dance_oauth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_dance_oauth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('provider', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('token', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.Column('provider_user_id', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='flask_dance_oauth_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='flask_dance_oauth_pkey'),
    sa.UniqueConstraint('provider_user_id', name='flask_dance_oauth_provider_user_id_key')
    )
    op.drop_table('buchregale')
    # ### end Alembic commands ###
