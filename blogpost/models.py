from django.db import models

# Create your models here.


class SampleModel (models.Model):
    title = models.CharField(max_length=100),
    number = models.IntegerField()


CATEGORY = (('business', 'Business'), ('life', 'Life'), ('other', 'Other'))


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdata = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY
    )
# Category はドロップダウンの選択肢　５行目にデファインされている

    def __str__(self) -> str:
        return self.title
