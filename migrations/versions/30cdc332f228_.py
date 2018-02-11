"""empty message

Revision ID: 30cdc332f228
Revises: 
Create Date: 2018-02-10 16:56:23.016531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30cdc332f228'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('custom_projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('panels',
    sa.Column('panel_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('width', sa.Numeric(), nullable=False),
    sa.Column('height', sa.Numeric(), nullable=False),
    sa.Column('thickness', sa.Numeric(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('panel_id')
    )
    op.create_table('pedestals',
    sa.Column('pedestal_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('width', sa.Numeric(), nullable=False),
    sa.Column('height', sa.Numeric(), nullable=False),
    sa.Column('depth', sa.Numeric(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('pedestal_id')
    )
    op.create_table('projects',
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('due_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('completion_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('project_title', sa.String(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('deposit', sa.Numeric(), nullable=True),
    sa.Column('discount', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('project_id')
    )
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
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('strainer_bars')
    op.drop_table('projects')
    op.drop_table('pedestals')
    op.drop_table('panels')
    op.drop_table('custom_projects')
    op.drop_table('clients')
    # ### end Alembic commands ###
