"""Second migration

Revision ID: fdf939f4d0db
Revises: f88549da3310
Create Date: 2021-05-31 12:58:49.753470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdf939f4d0db'
down_revision = 'f88549da3310'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('microblog_posts', sa.Column('preview', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('microblog_posts', 'preview')
    # ### end Alembic commands ###
