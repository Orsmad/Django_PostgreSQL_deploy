from django.db import models
import uuid


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=40,editable=True)
    text = models.TextField(max_length=450,null=True, blank=True,editable=True)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    upd_date = models.DateTimeField(auto_now=True)
    completed= models.BooleanField(default=False,null=True, blank=True,editable=True)

    def __str__(self) -> str:
        return self.title

 