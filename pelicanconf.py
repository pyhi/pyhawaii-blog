#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

AUTHOR = 'Stephan Fitzpatrick'
SITENAME = 'PyHawaii'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('HiCapacity', 'http://hicapacity.org'),
         ('The Box Jelly', 'http://theboxjelly.com/'),
        #  ('Jinja2', 'http://jinja.pocoo.org/'),
        #  ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (("Stephan's Twitter", 'http://twitter.com/knowsuchagency'),
          ("PyHawaii's Twitter", 'http://twitter.com/py_hawaii'),
          )

DEFAULT_PAGINATION = 10

# For plugins
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']

# Top-level directory for themes
THEME_ROOT = os.path.expanduser('~/git/pelican-themes/')

# Theme
THEME = os.path.join('.', 'themes', 'subtle')


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# For pelican elegant theme
LANDING_PAGE_ABOUT = {'title': 'Test Title',
'details': "I'm just a code ninja"}
