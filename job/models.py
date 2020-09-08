from django.db import models


JOB_TYPE = (
    ('Full time','Full time'),
    ('Part time',' Part time'),
)

# Create your models here.

class Job (models.Model):
    title = models.CharField(max_length=100)
    #Location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField (default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    


