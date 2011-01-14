import logging
import re

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate

from sqlalchemy import sql
from sqlalchemy import orm
import formencode as fe

from kronsztadt.lib.base import BaseController, render
from kronsztadt import model as m

log = logging.getLogger(__name__)

class SlugValidator(fe.FancyValidator):
    messages = {
        'bad_slug': 'This is not a valid slug'
    }
    def validate_python(self, value, state):
        if not re.match('[a-z-]+$', value):
            raise fe.Invalid(self.message('bad_slug', state),
                             value, state
                            )


class NewEntrySchema(fe.Schema):
    slug = SlugValidator()
    content_pol = fe.validators.String()
    content_rus = fe.validators.String()

class EntriesController(BaseController):

    def random(self):
        while True:
            try:
                entry = m.Session.query(m.Entry).filter(
                    Entry.rnd > randint(0, 2**16 - 1)
                ).limit(1).one()
            except orm.exc.NoResultFound:
                pass
            else:
                redirect(
                    controller = 'entries', action = 'get_by_slug',
                    slug = entry.slug
                )

    def get_by_slug(self, slug, lang = None):
        try:
            entry = m.Session.query(m.Entry).filter(
                Entry.slug = slug
            ).limit(1).one()
        except orm.exc.NoResultFound:
            abort(404)
        if lang is None:
            for l in request.languages:
                if l in ['pl', 'pl-pl']:
                    c.lang = 'pol'
            else:
                c.lang = 'rus'
        c.entry = entry
        return render('entries/display.mako')


    def form (self):
        return render('entries/form.mako')

    @validate(schema = NewEntrySchema, form = 'form')
    def new_entry(self):
        entry = m.Entry(
            self.form_result['slug'],
            {
                'pol': self.form_result['content_pol'],
                'rus': self.form_result['content_rus'],
            }
        )
        m.meta.Session.add(entry)
        m.meta.Session.commit()
        redirect('/')

