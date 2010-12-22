import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from sqlalchemy import sql

from kronsztadt.lib.base import BaseController, render
from kronsztadt import model as m

log = logging.getLogger(__name__)

class NewEntryValidator(fe.Schema):
    content_pol = fe.validators.String()
    content_rus = fe.validators.String()

class EntriesController(BaseController):

    # def random(self):
    #     entry = m.Session.query(m.Entry).innerjoin(m.Translation).\
    #             order_by(sql.functions.random()).limit(1).one()

    def form (self):
        return render('entries/form.mako')

    def new_entry(self):
