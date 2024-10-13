"""Adiciona campo endereco

Revision ID: 86f781860a71
Revises: 6793dd0d167a
Create Date: 2024-10-13 02:15:30.310615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f781860a71'
down_revision = '6793dd0d167a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endereco', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.drop_column('endereco')

    # ### end Alembic commands ###
