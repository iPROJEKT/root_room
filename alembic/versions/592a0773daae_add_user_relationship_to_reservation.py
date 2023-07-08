"""Add user relationship to Reservation

Revision ID: 592a0773daae
Revises: c87dfe788fd1
Create Date: 2023-07-08 20:58:18.153265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '592a0773daae'
down_revision = 'c87dfe788fd1'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        # В этой строке вместо None укажите название внешнего ключа.
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])


def downgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        # В этой строке вместо None укажите название внешнего ключа.
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
