from django.db import models

# Create your models here.
from django.utils import timezone


class TaskStatus(models.TextChoices):
    PENDING = 'PE','Pending'
    COMPLETED = 'CO', 'Completed'
    DROPPED = 'DR' ,'Dropped'

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(
        default= timezone.now()
    )
    deadline = models.DateTimeField( null = True , blank = True)
    status = models.CharField(
        choices=TaskStatus.choices,
        max_length=2,
        default=TaskStatus.PENDING
    )
    completed_at = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag,null=True)

    @property
    def foo(self):
        return "hello"

    def __str__(self):
        return f'{self.content}';

    def get_all_tags (self,delimeter=','):
         return delimeter.join([tag.name for tag in self.tags.all()])

