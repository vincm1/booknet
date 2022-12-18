"""empty message

Revision ID: 9389b59b06ab
Revises: 7847afee2376
Create Date: 2022-12-18 12:26:51.992315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9389b59b06ab'
down_revision = '7847afee2376'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('titel', sa.String(length=300), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('isbn', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('titel')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
