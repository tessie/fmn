from fmn.rules.ansible import *
from fmn.rules.askbot import *
from fmn.rules.bodhi import *
from fmn.rules.buildsys import *
from fmn.rules.compose import *
from fmn.rules.fas import *
from fmn.rules.fedbadges import *
from fmn.rules.fedoratagger import *
from fmn.rules.generic import *
from fmn.rules.git import *
from fmn.rules.mailman import *
from fmn.rules.meetbot import *
from fmn.rules.pkgdb import *
from fmn.rules.planet import *
from fmn.rules.trac import *
from fmn.rules.wiki import *


def DevelopmentRule(*args, **kwargs):
    """ All messages

    This lets every message through not matter the content.

    (Useful for development)
    """
    return True
