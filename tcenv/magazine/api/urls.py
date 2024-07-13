from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MagazineSubscriberViewSet, SubscriptionViewSet, SubscriptionPlanViewSet, SubscriberCategoryViewSet, SubscriberTypeViewSet, SubscriptionLanguageViewSet, SubscriptionModeViewSet, PaymentModeViewSet

router = DefaultRouter()
router.register(r'subscribers', MagazineSubscriberViewSet, basename='subscriber')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'subscription-plans', SubscriptionPlanViewSet, basename='subscriptionplan')
router.register(r'subscriber-categories', SubscriberCategoryViewSet, basename='subscribercategory')
router.register(r'subscriber-types', SubscriberTypeViewSet, basename='subscribertype')
router.register(r'subscription-languages', SubscriptionLanguageViewSet, basename='subscriptionlanguage')
router.register(r'subscription-modes', SubscriptionModeViewSet, basename='subscriptionmode')
router.register(r'payment-modes', PaymentModeViewSet, basename='paymentmode')

urlpatterns = [
    path('', include(router.urls)),
]
