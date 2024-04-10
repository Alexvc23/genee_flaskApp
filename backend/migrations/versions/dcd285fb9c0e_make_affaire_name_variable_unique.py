"""Make affaire name variable unique

Revision ID: dcd285fb9c0e
Revises: f0ea55ed68cd
Create Date: 2024-04-10 11:18:26.642409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcd285fb9c0e'
down_revision = 'f0ea55ed68cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('affaires', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['Nom'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('affaires', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###