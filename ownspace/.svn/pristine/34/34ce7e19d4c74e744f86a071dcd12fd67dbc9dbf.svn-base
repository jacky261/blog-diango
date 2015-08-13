import sae
import os
import sys
import pylibmc
import sys
sys.modules['memcache'] = pylibmc
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

from BBS import wsgi
application=sae.create_wsgi_app(wsgi.application)
