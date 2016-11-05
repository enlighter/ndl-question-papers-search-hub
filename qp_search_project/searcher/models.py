from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

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

LANGUAGES = (
    ('en', gettext_noop('English')),
    ('hi', gettext_noop('Hindi')),
    ('bn', gettext_noop('Bengali')),
)


class board(models.Model):
    name = models.CharField(max_length=15)
    #example : name = CBSE


    def __str__(self):
        return self.name

class exam(models.Model):
    name = models.CharField(max_length=15)
    # example : type = AISSCE


    def __str__(self):
        return self.name


class educational_institute(models.Model):
    name = models.CharField(max_length=90, unique=True)
    state = models.CharField(max_length=21, choices=in_states.STATE_CHOICES)
    city = models.CharField(max_length=21)


    def __str__(self):
        return self.name


class student(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    state = models.CharField(max_length=21, null=True, blank=True, choices=in_states.STATE_CHOICES)
    city = models.CharField(max_length=21, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    educational_role = models.CharField(max_length=39, choices=EDUCATIONAL_ROLE)
    institute = models.ForeignKey(educational_institute, null=True, blank=True)
    language = models.CharField(max_length=8, choices=LANGUAGES)


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create student instance on access - very useful if you plan to always have a Student obj associated with a User object anyway
User.student = property(lambda u: student.objects.get_or_create(user=u)[0])


class search_result(models.Model):
    year_month = models.DateField()
    type = models.ForeignKey(exam, on_delete=models.CASCADE)
    source = models.ForeignKey(board, null=True, blank=True)
    subject = models.CharField(max_length=45)
    location = models.URLField(max_length=120)


    def get_year(self):
        return self.year_month.year

    def get_month(self):
        return self.year_month.month

    def __str__(self):
        return str(self.get_year()) + str(self.type) + self.subject