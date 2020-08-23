from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField()
    origin_link = models.URLField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("post-detail", kwargs={"pk": self.pk})
