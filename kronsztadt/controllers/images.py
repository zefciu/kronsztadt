import logging

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect

from kronsztadt.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ImagesController(BaseController):

    def rnd(self):
        d = os.listdir(
            os.path.join(config['pylons.paths']['static_files']), 'images'
        )
