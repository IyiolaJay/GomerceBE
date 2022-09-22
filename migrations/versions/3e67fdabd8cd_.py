"""empty message

Revision ID: 3e67fdabd8cd
Revises: c2f0700e652a
Create Date: 2022-09-22 07:31:26.323261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e67fdabd8cd'
down_revision = 'c2f0700e652a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coupons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coupon_code', sa.Integer(), nullable=False),
    sa.Column('coupon_amount', sa.Float(), nullable=False),
    sa.Column('coupon_expiring_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('coupon_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupons')
    # ### end Alembic commands ###
