# -*- coding: utf-8 -*-
from froide.settings import Base, ThemeBase, HerokuPostmark, HerokuPostmarkS3  # noqa


class CustomThemeBase(ThemeBase):
    FROIDE_THEME = 'froide_theme.theme'

    SITE_NAME = "My Froide"
    SITE_EMAIL = "info@example.com"
    SITE_URL = 'http://localhost:8000'

    SECRET_URLS = {
        "admin": "admin",
    }


class Dev(CustomThemeBase, Base):
    pass


class ThemeHerokuPostmark(CustomThemeBase, HerokuPostmark):
    pass


class ThemeHerokuPostmarkS3(CustomThemeBase, HerokuPostmarkS3):
    pass


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
