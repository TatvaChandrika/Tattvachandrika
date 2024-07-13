<template>
  <div class="modal fade show" tabindex="-1" role="dialog" style="display: block;" v-if="show">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Add Subscription</h5>
          <button type="button" class="close" @click="close" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="save">
            <div class="form-group">
              <label for="subscription_plan">Subscription Plan</label>
              <select class="form-control" id="subscription_plan" v-model="form.subscription_plan" required>
                <option v-for="plan in plans" :key="plan._id" :value="plan._id">{{ plan.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="start_date">Start Date</label>
              <input type="date" class="form-control" id="start_date" v-model="form.start_date" disabled>
            </div>
            <div class="form-group">
              <label for="end_date">End Date</label>
              <input type="date" class="form-control" id="end_date" v-model="form.end_date" disabled>
            </div>
            <button type="submit" class="btn btn-primary">Add Subscription</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    subscriberId: String,
    plans: Array
  },
  data() {
    return {
      form: {
        subscriber: this.subscriberId,
        subscription_plan: '',
        start_date: this.calculateStartDate(),
        end_date: ''
      }
    };
  },
  watch: {
    'form.subscription_plan'(newPlanId) {
      const selectedPlan = this.plans.find(plan => plan._id === newPlanId);
      if (selectedPlan) {
        this.form.end_date = this.calculateEndDate(selectedPlan.duration_in_months);
      }
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    save() {
      this.$emit('save', { ...this.form });
    },
    calculateStartDate() {
      const today = new Date();
      const nextMonth = today.getMonth() === 11 ? 0 : today.getMonth() + 1;
      const nextYear = nextMonth === 0 ? today.getFullYear() + 1 : today.getFullYear();
      return new Date(nextYear, nextMonth, 10).toISOString().split('T')[0];
    },
    calculateEndDate(durationInMonths) {
      const startDate = new Date(this.form.start_date);
      const endYear = startDate.getFullYear() + Math.floor((startDate.getMonth() + durationInMonths) / 12);
      const endMonth = (startDate.getMonth() + durationInMonths) % 12;
      const endDate = new Date(endYear, endMonth, 0); // 0 will give the last day of the previous month
      return endDate.toISOString().split('T')[0];
    }
  }
};
</script>

<style scoped>
.modal {
  display: block;
  background-color: rgba(0, 0, 0, 0.5);
}
</style>
