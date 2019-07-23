"""empty message

Revision ID: f43bc7e6702f
Revises: 
Create Date: 2019-07-14 11:24:49.398817

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f43bc7e6702f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('ygdy')
    op.drop_table('person')
    op.drop_table('xicidaili')
    op.drop_table('douban_movie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('douban_movie',
    sa.Column('id', mysql.BIGINT(display_width=9), autoincrement=True, nullable=False),
    sa.Column('directors', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('rate', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=4), nullable=False),
    sa.Column('cover_x', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('star', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=5), nullable=False),
    sa.Column('title', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=50), nullable=False),
    sa.Column('url', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=100), nullable=False),
    sa.Column('casts', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('cover', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=100), nullable=False),
    sa.Column('movie_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=12), nullable=False),
    sa.Column('cover_y', mysql.VARCHAR(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('xicidaili',
    sa.Column('id', mysql.INTEGER(display_width=5), autoincrement=True, nullable=False),
    sa.Column('ip', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('port', mysql.VARCHAR(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('person',
    sa.Column('person_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('person_name', mysql.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('person_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('ygdy',
    sa.Column('id', mysql.INTEGER(display_width=7), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(charset='gb2312', collation='gb2312_chinese_ci', length=255), nullable=True),
    sa.Column('ftp', mysql.VARCHAR(charset='gb2312', collation='gb2312_chinese_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('student')
    # ### end Alembic commands ###
