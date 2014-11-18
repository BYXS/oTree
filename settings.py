

import os
import otree.settings
import dj_database_url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


OTREE_PRODUCTION = os.environ.get('OTREE_PRODUCTION')
if OTREE_PRODUCTION:
    DEBUG = False
else:
    DEBUG = True


# set the below env var on servers that participants will see,
    # since they should not be able to access the demo page
OTREE_PARTICIPANT_FACING_SITE = os.environ.get('OTREE_PARTICIPANT_FACING_SITE')


IS_OTREE_DOT_ORG = os.environ.get('IS_OTREE_DOT_ORG')
if IS_OTREE_DOT_ORG:
    ADMIN_PASSWORD = os.environ['OTREE_ADMIN_PASSWORD']
    SECRET_KEY = os.environ['OTREE_SECRET_KEY']
else:
    ADMIN_PASSWORD = 'otree'
    # don't share this with anybody.
    # Change this to something unique (e.g. mash your keyboard), and
    # then delete this comment.
    SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'


DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///{}/{}'.format(BASE_DIR, 'db.sqlite3')
    )
}


CREATE_DEFAULT_SUPERUSER = True
ADMIN_USERNAME = 'admin'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# e.g. EUR, CAD, GBP, CHF, CNY, JPY
PAYMENT_CURRENCY_CODE = 'EUR'
USE_POINTS = True

# e.g. en-gb, de-de, it-it, fr-fr. see: https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

INSTALLED_APPS = [
    'otree',
    'raven.contrib.django.raven_compat',
]

INSTALLED_OTREE_APPS = [
    'demo_game',
    'trust',
    'lab_results',
    'public_goods',
    'prisoner',
    'cournot_competition',
    'dictator',
    'matching_pennies',
    'traveler_dilemma',
    'survey',
    'bargaining',
    'beauty',
    'common_value_auction',
    'matrix_symmetric',
    'matrix_asymmetric',
    'stackelberg_competition',
    'vickrey_auction',
    'volunteer_dilemma',
    'bertrand_competition',
    'principal_agent',
    'stag_hunt',
    'battle_of_the_sexes',
    'survey_sample',
    'asset_market',
    'lemon_market',
    'feedback',
]


WSGI_APPLICATION = 'wsgi.application'

SESSIONS_MODULE = 'sessions'

ACCESS_CODE_FOR_OPEN_SESSION = 'idd1610'

otree.settings.augment_settings(globals())

