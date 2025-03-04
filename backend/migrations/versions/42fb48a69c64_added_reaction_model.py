"""Added Reaction model

Revision ID: 42fb48a69c64
Revises: 
Create Date: 2024-08-18 12:14:30.700411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42fb48a69c64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('beat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('caption', sa.String(length=512), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('beat', schema=None) as batch_op:
        batch_op.drop_column('caption')

    # ### end Alembic commands ###
