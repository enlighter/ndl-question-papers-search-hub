from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

from localflavor.in_ import in_states


gettext_noop = lambda s: s
EDUCATIONAL_ROLE= (
    ('vb', gettext_noop('Till Class VIII')),
    ('mc', gettext_noop('Class IX to X')),
    ('ss', gettext_noop('Class XI to XII')),
    ('gr', gettext_noop('UG or PG')),
    ('cd', gettext_noop('Career Development or Technical Study')),
    ('ae', gettext_noop('Adult Education')),
    ('ll', gettext_noop('Lifelong Learner')),
)


class student(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    state = models.CharField(max_length=21, null=True, blank=True, choices=in_states.STATE_CHOICES)
    city = models.CharField(max_length=21, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    educational_role = models.CharField(max_length=39, choices=EDUCATIONAL_ROLE)
    institute = models.CharField(max_length=99, null=True, blank=True)
    language = models.CharField(max_length=8, choices=settings.LANGUAGES)
