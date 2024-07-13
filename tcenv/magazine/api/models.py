import mongoengine as me
import datetime
import calendar
from .utils import generate_id

class SubscriberCategory(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('SCAT', 'subscriber_category'))
    name = me.StringField(max_length=255, unique=True)

class SubscriberType(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('STYPE', 'subscriber_type'))
    name = me.StringField(max_length=255, unique=True)

class SubscriptionLanguage(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('SLANG', 'subscription_language'))
    name = me.StringField(max_length=50, unique=True)

class SubscriptionMode(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('SMODE', 'subscription_mode'))
    name = me.StringField(max_length=50, unique=True)

class SubscriptionPlan(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('SPLAN', 'subscription_plan'))
    version = me.StringField(max_length=10)
    name = me.StringField(max_length=255)
    start_date = me.DateField()
    subscription_price = me.DecimalField()
    subscription_language = me.ReferenceField(SubscriptionLanguage, null=True)
    subscription_mode = me.ReferenceField(SubscriptionMode, null=True)
    duration_in_months = me.IntField()  # Duration in months

    def save(self, *args, **kwargs):
        if not self.version:
            self.version = self.generate_version()
        self.name = f"{self.duration_in_months} months - {self.subscription_language.name} - {self.subscription_mode.name}"
        super(SubscriptionPlan, self).save(*args, **kwargs)

    def generate_version(self):
        existing_plans = SubscriptionPlan.objects(
            subscription_language=self.subscription_language,
            subscription_mode=self.subscription_mode,
            duration_in_months=self.duration_in_months
        ).order_by('-version')

        if existing_plans:
            latest_plan = existing_plans.first()
            if latest_plan.subscription_price == self.subscription_price:
                return latest_plan.version
            else:
                latest_version_number = int(latest_plan.version[1:])
                return f"v{latest_version_number + 1}"
        else:
            return "v1"

class MagazineSubscriber(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('SUBS', 'subscriber'))
    name = me.StringField(max_length=255)
    registration_number = me.StringField(max_length=255, unique=True)
    address = me.StringField()
    city_town = me.StringField(max_length=255)
    state = me.StringField(max_length=255)
    pincode = me.StringField(max_length=10)
    phone = me.StringField(max_length=15)
    email = me.EmailField(unique=True)
    category = me.ReferenceField(SubscriberCategory, null=True)
    stype = me.ReferenceField(SubscriberType, null=True)
    notes = me.StringField()
    active = me.BooleanField(default=True)
    
class Subscription(me.Document):
    _id = me.StringField(primary_key=True, default=lambda: generate_id('SUBSCR', 'subscription'))
    subscriber = me.ReferenceField(MagazineSubscriber, reverse_delete_rule=me.CASCADE)
    subscription_plan = me.ReferenceField(SubscriptionPlan, null=True)
    start_date = me.DateField()
    end_date = me.DateField()
    active = me.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.start_date = self.calculate_start_date()
        self.end_date = self.calculate_end_date()
        super(Subscription, self).save(*args, **kwargs)

    def calculate_start_date(self):
        today = datetime.date.today()
        next_month = today.month + 1 if today.month < 12 else 1
        next_year = today.year if next_month != 1 else today.year + 1
        return datetime.date(next_year, next_month, 10)

    def calculate_end_date(self):
        duration = self.subscription_plan.duration_in_months
        start_date = self.start_date
        end_year = start_date.year + ((start_date.month + duration - 1) // 12)
        end_month = (start_date.month + duration - 1) % 12 + 1
        last_day_of_month = calendar.monthrange(end_year, end_month)[1]
        return datetime.date(end_year, end_month, last_day_of_month)
