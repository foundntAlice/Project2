from django.apps import AppConfig
from django.db import DatabaseError
from django.utils.translation import gettext_lazy


class JudgeAppConfig(AppConfig):
    name = 'judge'
    verbose_name = gettext_lazy('Online Judge')

    def ready(self):
        from . import signals, jinja2

        from judge.models import Language, Profile
        from django.contrib.auth.models import User

        try:
            lang = Language.get_default_language()
            for user in User.objects.filter(profile=None):
                profile = Profile(user=user, language=lang)
                profile.save()
        except DatabaseError:
            pass
