"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from kronsztadt.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

entries_table = sa.Table(
    'entries', meta.metadata,
    sa.Column('id', sa.types.Integer(), sa.Sequence('entries_id_seq'), primary_key = True),
    sa.Column('slug', sa.types.Unicode(64)),
    sa.Column('rnd', sa.types.Integer()),
)

translations_table = sa.Table(
    'translations', meta.metadata,
    sa.Column('entry_id', sa.types.Integer, sa.ForeignKey('entries.id'), primary_key = True),
    sa.Column('language', sa.types.String(3), primary_key = True),
    sa.Column('content', sa.types.UnicodeText()),
)

class Translation(object):

    def __init__(self, language, content):
        self.language = language
        self.content = content


class Entry(object):

    def __init__(self, slug, translations):
        self.slug = slug
        self.rnd = randint(0, 2**16 - 1)
        self.translations.append(Translation(t, translations[t]))


orm.mapper(Entry, entries_table, properties = {
    'translations': orm.relationship(Translation, backref = 'entry')
})

orm.mapper(Translation, translations_table)
