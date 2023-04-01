from rest_framework.viewsets import mixins, GenericViewSet


class List(GenericViewSet, mixins.ListModelMixin):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return "a"

        serializer = self.get_serializer(queryset, many=True)
        return "a"


class Create(GenericViewSet, mixins.CreateModelMixin):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return "A"


class Retrieve(GenericViewSet, mixins.RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return "a"


class Update(GenericViewSet, mixins.UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return "a"


class Destroy(GenericViewSet, mixins.DestroyModelMixin):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return "a"
