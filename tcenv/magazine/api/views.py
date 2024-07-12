from rest_framework_mongoengine import viewsets
from .models import MagazineSubscriber, Subscription, SubscriptionPlan, SubscriberCategory, SubscriberType, SubscriptionLanguage, SubscriptionMode
from .serializers import MagazineSubscriberSerializer, SubscriptionSerializer, SubscriptionPlanSerializer, SubscriberCategorySerializer, SubscriberTypeSerializer, SubscriptionLanguageSerializer, SubscriptionModeSerializer

class SubscriberCategoryViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriberCategorySerializer

    def get_queryset(self):
        return SubscriberCategory.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriberTypeViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriberTypeSerializer

    def get_queryset(self):
        return SubscriberType.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionLanguageViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionLanguageSerializer

    def get_queryset(self):
        return SubscriptionLanguage.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionModeViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionModeSerializer

    def get_queryset(self):
        return SubscriptionMode.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionPlanSerializer

    def get_queryset(self):
        return SubscriptionPlan.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class MagazineSubscriberViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = MagazineSubscriberSerializer

    def get_queryset(self):
        return MagazineSubscriber.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
