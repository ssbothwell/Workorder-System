"""empty message

Revision ID: 5ca83a02e934
Revises: f5ec641664e5
Create Date: 2018-02-12 08:02:34.692334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ca83a02e934'
down_revision = 'f5ec641664e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('custom_projects', sa.Column('p_type', sa.String(), nullable=False))
    op.add_column('panels', sa.Column('p_type', sa.String(), nullable=False))
    op.add_column('pedestals', sa.Column('p_type', sa.String(), nullable=False))
    op.add_column('strainer_bars', sa.Column('p_type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('strainer_bars', 'p_type')
    op.drop_column('pedestals', 'p_type')
    op.drop_column('panels', 'p_type')
    op.drop_column('custom_projects', 'p_type')
    # ### end Alembic commands ###
