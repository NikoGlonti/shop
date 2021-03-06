"""book_author.author_id field fixed

Revision ID: aea4c174073a
Revises: e66198605431
Create Date: 2022-05-04 14:24:18.528000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aea4c174073a'
down_revision = 'e66198605431'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books_authors', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_constraint('books_authors_author-id_fkey', 'books_authors', type_='foreignkey')
    op.create_foreign_key(None, 'books_authors', 'author', ['author_id'], ['id'])
    op.drop_column('books_authors', 'author-id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books_authors', sa.Column('author-id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'books_authors', type_='foreignkey')
    op.create_foreign_key('books_authors_author-id_fkey', 'books_authors', 'author', ['author-id'], ['id'])
    op.drop_column('books_authors', 'author_id')
    # ### end Alembic commands ###
