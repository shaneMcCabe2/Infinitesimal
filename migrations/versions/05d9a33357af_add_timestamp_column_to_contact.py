"""add timestamp column to contact

Revision ID: 05d9a33357af
Revises: fbfff0d509a6
Create Date: 2022-12-13 09:55:33.796017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05d9a33357af'
down_revision = 'fbfff0d509a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_contact_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_contact_timestamp'))
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###