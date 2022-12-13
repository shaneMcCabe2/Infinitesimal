"""contact table

Revision ID: fbfff0d509a6
Revises: 
Create Date: 2022-12-13 09:33:27.935833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbfff0d509a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('body', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_contact_body'), ['body'], unique=True)
        batch_op.create_index(batch_op.f('ix_contact_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_contact_first_name'), ['first_name'], unique=True)
        batch_op.create_index(batch_op.f('ix_contact_last_name'), ['last_name'], unique=True)
        batch_op.create_index(batch_op.f('ix_contact_phone'), ['phone'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_contact_phone'))
        batch_op.drop_index(batch_op.f('ix_contact_last_name'))
        batch_op.drop_index(batch_op.f('ix_contact_first_name'))
        batch_op.drop_index(batch_op.f('ix_contact_email'))
        batch_op.drop_index(batch_op.f('ix_contact_body'))

    op.drop_table('contact')
    # ### end Alembic commands ###