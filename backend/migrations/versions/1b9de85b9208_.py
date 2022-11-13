"""empty message

Revision ID: 1b9de85b9208
Revises: bc222e7dd68c
Create Date: 2022-11-13 19:54:32.846526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b9de85b9208'
down_revision = 'bc222e7dd68c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Post', sa.Column('image', sa.String(length=255), nullable=True))
    op.add_column('User', sa.Column('image', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'image')
    op.drop_column('Post', 'image')
    # ### end Alembic commands ###