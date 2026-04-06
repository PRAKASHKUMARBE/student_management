from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    course = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to='student_photos/',
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
# Create your models here.
