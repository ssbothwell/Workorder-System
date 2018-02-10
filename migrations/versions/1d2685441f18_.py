"""empty message

Revision ID: 1d2685441f18
Revises: db5974dcce66
Create Date: 2018-02-07 23:03:59.336464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d2685441f18'
down_revision = 'db5974dcce66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('strainer_bars',
    sa.Column('strainer_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('width', sa.Numeric(), nullable=False),
    sa.Column('height', sa.Numeric(), nullable=False),
    sa.Column('thickness', sa.Numeric(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('strainer_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('strainer_bars')
    # ### end Alembic commands ###
