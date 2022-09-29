from rest_framework import mixins, viewsets


class ViewDeleteSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
):

    pass
