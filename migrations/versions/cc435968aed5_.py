"""empty message

Revision ID: cc435968aed5
Revises: 30cdc332f228
Create Date: 2018-02-10 22:17:50.900513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc435968aed5'
down_revision = '30cdc332f228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('panels', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('panels', 'panel_id')
    op.add_column('pedestals', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('pedestals', 'pedestal_id')
    op.add_column('projects', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('projects', 'client_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'projects', 'clients', ['client_id'], ['id'])
    op.drop_column('projects', 'project_id')
    op.add_column('strainer_bars', sa.Column('iner_id', sa.Integer(), nullable=False))
    op.drop_column('strainer_bars', 'strainer_id')
    op.add_column('users', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.INTEGER(), nullable=False))
    op.drop_column('users', 'id')
    op.add_column('strainer_bars', sa.Column('strainer_id', sa.INTEGER(), nullable=False))
    op.drop_column('strainer_bars', 'iner_id')
    op.add_column('projects', sa.Column('project_id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.alter_column('projects', 'client_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('projects', 'id')
    op.add_column('pedestals', sa.Column('pedestal_id', sa.INTEGER(), nullable=False))
    op.drop_column('pedestals', 'id')
    op.add_column('panels', sa.Column('panel_id', sa.INTEGER(), nullable=False))
    op.drop_column('panels', 'id')
    # ### end Alembic commands ###
