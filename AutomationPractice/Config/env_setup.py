import os


class EnvSetup(object):

    # ENV VAR that defines the main URL (Domain)
    SITE = os.getenv('BASE_URL', 'http://automationpractice.com')

