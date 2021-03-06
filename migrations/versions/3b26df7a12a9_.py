"""empty message

Revision ID: 3b26df7a12a9
Revises: None
Create Date: 2014-01-24 10:55:15.076255

"""

# revision identifiers, used by Alembic.
revision = '3b26df7a12a9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('mood', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # op.drop_index('user_phone_number_key', 'user')
    # op.drop_index('user_username_url_key', 'user')
    op.create_unique_constraint(None, 'user', ['phone_number'])
    op.create_unique_constraint(None, 'user', ['username_url'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user')
    op.drop_constraint(None, 'user')
    # op.create_index('user_username_url_key', 'user', [u'username_url'], unique=True)
    # op.create_index('user_phone_number_key', 'user', [u'phone_number'], unique=True)
    op.drop_table('entry')
    ### end Alembic commands ###
