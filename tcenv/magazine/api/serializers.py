from rest_framework_mongoengine import serializers
from .models import MagazineSubscriber, Subscription, SubscriptionPlan, SubscriberCategory, SubscriberType, SubscriptionLanguage, SubscriptionMode

class SubscriberCategorySerializer(serializers.DocumentSerializer):
    class Meta:
        model = SubscriberCategory
        fields = ('_id', 'name')

class SubscriberTypeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = SubscriberType
        fields = ('_id', 'name')

class SubscriptionLanguageSerializer(serializers.DocumentSerializer):
    class Meta:
        model = SubscriptionLanguage
        fields = ('_id', 'name')

class SubscriptionModeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = SubscriptionMode
        fields = ('_id', 'name')

class SubscriptionPlanSerializer(serializers.DocumentSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ('_id', 'version', 'name', 'start_date', 'subscription_price', 'subscription_language', 'subscription_mode', 'duration_in_months')

class SubscriptionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class MagazineSubscriberSerializer(serializers.DocumentSerializer):
    subscriptions = SubscriptionSerializer(many=True, read_only=True)

    class Meta:
        model = MagazineSubscriber
        fields = '__all__'
