"""empty message

Revision ID: f51557cbefc5
Revises: None
Create Date: 2016-05-24 14:11:10.722614

"""

# revision identifiers, used by Alembic.
revision = 'f51557cbefc5'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.String(length=120), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'bio')
    ### end Alembic commands ###
