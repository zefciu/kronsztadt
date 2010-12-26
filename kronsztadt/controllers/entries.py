import logging
import re

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate

from sqlalchemy import sql
import formencode as fe

from kronsztadt.lib.base import BaseController, render
from kronsztadt import model as m

log = logging.getLogger(__name__)

class SlugValidator(fe.FancyValidator):
    messages = {
        'bad_slug': 'This is not a valid slug'
    }
    def validate_python(self, value, state):
        if re.match('[a-z-]+$', value):
            raise re.Invalid(self.message('bad_slug', state),
                             value, state
                            )


class NewEntrySchema(fe.Schema):
    slug = SlugValidator()
    content_pol = fe.validators.String()
    content_rus = fe.validators.String()

class EntriesController(BaseController):

    # def random(self):
    #     entry = m.Session.query(m.Entry).innerjoin(m.Translation).\
    #             order_by(sql.functions.random()).limit(1).one()

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
        m.Session.add(entry)
        m.Session.commit()
        redirect('/')

