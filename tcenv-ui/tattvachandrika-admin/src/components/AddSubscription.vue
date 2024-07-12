<template>
  <div class="container mt-5">
    <h2>Add Subscription for {{ subscriberName }}</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item"><router-link to="/subscribers">Magazine Subscribers</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Add Subscription</li>
      </ol>
    </nav>

    <form @submit.prevent="addSubscription">
      <div class="mb-3">
        <label for="subscription_plan">Subscription Plan</label>
        <select id="subscription_plan" v-model="subscriptionForm.subscription_plan" class="form-control">
          <option v-for="plan in subscriptionPlans" :key="plan._id" :value="plan._id">{{ plan.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="start_date">Start Date</label>
        <input
          type="date"
          id="start_date"
          v-model="subscriptionForm.start_date"
          placeholder="Start Date"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="active">Active</label>
        <input
          type="checkbox"
          id="active"
          v-model="subscriptionForm.active"
          class="form-check-input"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Add Subscription</button>
    </form>
  </div>
</template>

<script>
import subscriptionService from '../services/subscriptionService';
import subscriptionPlanService from '../services/subscriptionPlanService';
import magazineSubscriberService from '../services/magazineSubscriberService';

export default {
  data() {
    return {
      subscriptionForm: {
        subscriber: this.$route.params.subscriberId,
        subscription_plan: '',
        start_date: '',
        end_date: '',
        active: true
      },
      subscriptionPlans: [],
      subscriberName: ''
    };
  },
  created() {
    this.loadSubscriptionPlans();
    this.loadSubscriberName();
  },
  methods: {
    loadSubscriptionPlans() {
      subscriptionPlanService.getSubscriptionPlans().then(response => {
        this.subscriptionPlans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadSubscriberName() {
      magazineSubscriberService.getMagazineSubscriberById(this.$route.params.subscriberId).then(response => {
        this.subscriberName = response.data.name;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber name!", error);
      });
    },
    calculateEndDate(startDate, durationInMonths) {
      const start = new Date(startDate);
      const end = new Date(start);
      end.setMonth(end.getMonth() + durationInMonths);
      return end.toISOString().split('T')[0]; // Format as YYYY-MM-DD
    },
    addSubscription() {
      const selectedPlan = this.subscriptionPlans.find(plan => plan._id === this.subscriptionForm.subscription_plan);
      if (selectedPlan) {
        this.subscriptionForm.end_date = this.calculateEndDate(this.subscriptionForm.start_date, selectedPlan.duration_in_months);
        subscriptionService.createSubscription(this.subscriptionForm).then(() => {
          this.$router.push('/subscribers');
        }).catch(error => {
          console.error("There was an error adding the subscription!", error);
        });
      }
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
