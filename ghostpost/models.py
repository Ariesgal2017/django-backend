from django.db import models
from django.utils import timezone

class RBModel(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content

    
    @property
    def vote_score(self):
        vote_sum = self.upvotes + self.downvotes
        return vote_sum