# vim: set fileencoding=utf-8 
"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
from webhelpers.html.tags import text, textarea, form, end_form, submit, link_to
from webhelpers.html.tags import image
from routes import url_for

import pylons
import os
import random as rnd

def random_img():
    d = os.listdir(os.path.join(pylons.config['pylons.paths']['static_files'], 'images'))
    return image('images/' + rnd.choice(d), 'Św. Jan z Kronsztadu')
