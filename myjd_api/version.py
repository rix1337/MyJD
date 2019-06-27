# -*- coding: utf-8 -*-
# MyJD
# Project by https://github.com/rix1337

import re
from distutils.version import StrictVersion as version

from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen


def get_version():
    return "v.0.2.0"
