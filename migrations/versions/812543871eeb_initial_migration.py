"""Initial migration.

Revision ID: 812543871eeb
Revises: 
Create Date: 2021-02-12 16:31:18.794147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '812543871eeb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('league',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team_league',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('league_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['league_id'], ['league.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('team_id', 'league_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_league')
    op.drop_table('team')
    op.drop_table('league')
    # ### end Alembic commands ###
