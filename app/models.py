from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

FIRST = "First"
SECOND = "Second"
THIRD = "Third"

SEMESTER = (
    (FIRST, "First"),
    (SECOND, "Second"),
    (THIRD, "Third"),
)


class NewsAndEventsQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(host__icontains=query) | 
                  Q(participants__icontains=query) |
                  Q(meet_time__icontains=query)|
                  Q(team_name__icontains=query) |
                  Q(summary__icontains=query) 
                  )
        return self.filter(lookups).distinct()


class NewsAndEventsManager(models.Manager):
    def get_queryset(self):
        return NewsAndEventsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # NewsAndEvents.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class NewsAndEvents(models.Model):
    host = models.CharField(max_length=200, null=True)
    participants= ArrayField(models.CharField(max_length=100), null=True)
    meet_time = models.CharField(max_length=200, null=True)
    team_name=models.CharField(max_length=200, null=True)
    summary = models.TextField(max_length=200, blank=True, null=True)
 

    objects = NewsAndEventsManager()

    def __str__(self):
        return self.host


class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session


class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    is_current_semester = models.BooleanField(default=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    next_semester_begins = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.semester
