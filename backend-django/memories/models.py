from django.db import models


class Memory(models.Model):
    title = models.TextField()
    description = models.TextField()
    published_at = models.DateTimeField("Date Published")
    owner = models.ForeignKey(
        "auth.User", related_name="memories", on_delete=models.CASCADE
    )
