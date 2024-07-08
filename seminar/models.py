from django.db import models

# Create your models here.
from .consts import MAX_RATE

RATE_CHOICES = [ (x, str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('business', 'ビジネス'), ('life', '生活'),('other', 'その他'))

class Seminar(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title 


class Video(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='seminar_videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} for {self.seminar.title}'
