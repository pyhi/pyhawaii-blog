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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        #  ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/knowsuchagency'),
        #   ('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# For plugins
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']

# Top-level directory for themes
THEME_ROOT = os.path.expanduser('~/pelican-themes/')

# Theme
THEME = os.path.join(THEME_ROOT, 'subtle')


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
