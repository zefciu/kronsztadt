"""The application's model objects"""
from random import randint

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
    sa.Column('slug', sa.types.Unicode(64), index = True, unique = True),
    sa.Column('rnd', sa.types.Integer(), index = True, unique = True),
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
        while True: # Birtday bound for random key is 300
            self.rnd = randint(0, 2**16 - 1)
            if not meta.Session.query(Entry).filter(
                Entry.rnd == self.rnd
            ).count():
                break
        for t in translations:
            self.translations.append(Translation(t, translations[t]))

    def get_trans(self, lang):
        for t in self.translations:
            if t.language == lang:
                return t
        return None


orm.mapper(Entry, entries_table, properties = {
    'translations': orm.relationship(Translation, backref = 'entry')
})

orm.mapper(Translation, translations_table)
