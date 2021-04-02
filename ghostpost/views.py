from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ghostpost.models import RBModel
from ghostpost.serializers import RBSerializer


# Create your views here.
class RBModelViewSet(viewsets.ModelViewSet):
    queryset = RBModel.objects.all()
    serializer_class = RBSerializer
    @action(detail=False)
    def boasts(self, request, pk=None):
        boasts_bydatetime = RBModel.objects.filter(is_boast=True).order_by('-post_datetime')
        serializer = self.get_serializer(boasts_bydatetime, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request, pk=None):
        roasts_bydatetime = RBModel.objects.filter(is_boast=False).order_by('-post_datetime')
        serializer = self.get_serializer(roasts_bydatetime, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        boast_or_roast = RBModel.objects.get(id=pk)
        boast_or_roast.upvotes += 1
        boast_or_roast.save()
        return Response('Upvoted Successfully')

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        boast_or_roast = RBModel.objects.get(id=pk)
        boast_or_roast.downvotes -= 1
        boast_or_roast.save()
        return Response('Downvoted Successfully')