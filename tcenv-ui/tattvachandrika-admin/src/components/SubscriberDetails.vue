<template>
  <div class="container mt-5">
    <h2>Subscriber Details: {{ subscriber.name }}</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item"><router-link to="/subscribers">Magazine Subscribers</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscriber Details</li>
      </ol>
    </nav>

    <div class="card mb-3">
      <div class="card-header">
        Subscriber Information
      </div>
      <div class="card-body">
        <p><strong>Name:</strong> {{ subscriber.name }}</p>
        <p><strong>Registration Number:</strong> {{ subscriber.registration_number }}</p>
        <p><strong>Address:</strong> {{ subscriber.address }}</p>
        <p><strong>City/Town:</strong> {{ subscriber.city_town }}</p>
        <p><strong>State:</strong> {{ subscriber.state }}</p>
        <p><strong>Pincode:</strong> {{ subscriber.pincode }}</p>
        <p><strong>Phone:</strong> {{ subscriber.phone }}</p>
        <p><strong>Email:</strong> {{ subscriber.email }}</p>
        <p><strong>Category:</strong> {{ getCategoryName(subscriber.category) }}</p>
        <p><strong>Type:</strong> {{ getTypeName(subscriber.stype) }}</p>
        <p><strong>Notes:</strong> {{ subscriber.notes }}</p>
        <p><strong>Active:</strong> {{ subscriber.active ? 'Yes' : 'No' }}</p>
      </div>
    </div>

    <h3>Subscriptions</h3>
    <table class="table table-striped mt-3">
      <thead>
        <tr>
          <th>Subscription Plan</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Active</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subscription in subscriptions" :key="subscription._id">
          <td>{{ getSubscriptionPlanName(subscription.subscription_plan) }}</td>
          <td>{{ subscription.start_date }}</td>
          <td>{{ subscription.end_date }}</td>
          <td>{{ subscription.active ? 'Yes' : 'No' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import magazineSubscriberService from '../services/magazineSubscriberService';
import subscriptionService from '../services/subscriptionService';
import subscriptionPlanService from '../services/subscriptionPlanService';
import subscriberCategoryService from '../services/subscriberCategoryService';
import subscriberTypeService from '../services/subscriberTypeService';

export default {
  data() {
    return {
      subscriber: {},
      subscriptions: [],
      subscriptionPlans: [],
      subscriberCategories: [],
      subscriberTypes: []
    };
  },
  created() {
    this.loadSubscriber();
    this.loadSubscriptions();
    this.loadSubscriptionPlans();
    this.loadSubscriberCategories();
    this.loadSubscriberTypes();
  },
  methods: {
    loadSubscriber() {
      magazineSubscriberService.getMagazineSubscriberById(this.$route.params.subscriberId).then(response => {
        this.subscriber = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber details!", error);
      });
    },
    loadSubscriptions() {
      subscriptionService.getSubscriptionsBySubscriberId(this.$route.params.subscriberId).then(response => {
        this.subscriptions = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriptions!", error);
      });
    },
    loadSubscriptionPlans() {
      subscriptionPlanService.getSubscriptionPlans().then(response => {
        this.subscriptionPlans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadSubscriberCategories() {
      subscriberCategoryService.getSubscriberCategories().then(response => {
        this.subscriberCategories = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber categories!", error);
      });
    },
    loadSubscriberTypes() {
      subscriberTypeService.getSubscriberTypes().then(response => {
        this.subscriberTypes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber types!", error);
      });
    },
    getSubscriptionPlanName(planId) {
      const plan = this.subscriptionPlans.find(p => p._id === planId);
      return plan ? plan.name : 'Unknown';
    },
    getCategoryName(categoryId) {
      const category = this.subscriberCategories.find(cat => cat._id === categoryId);
      return category ? category.name : 'Unknown';
    },
    getTypeName(typeId) {
      const type = this.subscriberTypes.find(typ => typ._id === typeId);
      return type ? type.name : 'Unknown';
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
