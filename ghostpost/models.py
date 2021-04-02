from django.db import models
from django.utils import timezone

class RBModel(models.Model):
    # Thanks Joe for the guidance (shared with the group at study hall), refer to https://docs.djangoproject.com/en/3.1/ref/models/fields/
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    # Ability to sort content based on vote score (hint: you may need to calculate the vote score)
    # https://docs.python.org/3/library/functions.html#property
    @property
    def vote_score(self):
        vote_sum = self.upvotes - self.downvotes
        return vote_sum