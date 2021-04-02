from rest_framework import serializers
from ghostpost.models import RBModel


# Worked with Sohail and Albina too on the planning/beginning stage before finishing separately
class RBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RBModel
        fields = [
            'id',
            'is_boast',
            'content',
            'upvotes',
            'downvotes',
            'post_time',
        ]