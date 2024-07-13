<template>
  <div class="container mt-5">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Plans</li>
      </ol>
    </nav>
    <h2>Subscription Plans</h2>
    <button class="btn btn-primary mb-3" @click="addPlan">Add Subscription Plan</button>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Version</th>
          <th>Start Date</th>
          <th>Price</th>
          <th>Language</th>
          <th>Mode</th>
          <th>Duration (Months)</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="plan in plans" :key="plan._id">
          <td>{{ plan.name }}</td>
          <td>{{ plan.version }}</td>
          <td>{{ plan.start_date }}</td>
          <td>
            <input v-if="editPlanId === plan._id" type="number" v-model="plan.subscription_price" />
            <span v-else>{{ plan.subscription_price }}</span>
          </td>
          <td>
            <select v-if="editPlanId === plan._id" v-model="plan.subscription_language" :key="plan._id + '_language'">
              <option v-for="language in languages" :value="language._id" :key="language._id">{{ language.name }}</option>
            </select>
            <span v-else>{{ getLanguageName(plan.subscription_language) }}</span>
          </td>
          <td>
            <select v-if="editPlanId === plan._id" v-model="plan.subscription_mode" :key="plan._id + '_mode'">
              <option v-for="mode in modes" :value="mode._id" :key="mode._id">{{ mode.name }}</option>
            </select>
            <span v-else>{{ getModeName(plan.subscription_mode) }}</span>
          </td>
          <td>
            <input v-if="editPlanId === plan._id" type="number" v-model="plan.duration_in_months" />
            <span v-else>{{ plan.duration_in_months }}</span>
          </td>
          <td>
            <button class="btn btn-success btn-sm" v-if="editPlanId === plan._id" @click="savePlan(plan)">Save</button>
            <button class="btn btn-warning btn-sm" v-else @click="editPlan(plan._id)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="confirmDeletePlan(plan._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription plan?"
      @close="hideDeleteModal"
      @confirm="deletePlan"
    />
  </div>
</template>

<script>
import subscriptionPlanService from '../services/subscriptionPlanService';
import confirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    confirmationModal
  },
  data() {
    return {
      plans: [],
      languages: [],
      modes: [],
      editPlanId: null,
      showConfirmationModal: false,
      planToDelete: null
    };
  },
  created() {
    this.loadPlans();
    this.loadLanguages();
    this.loadModes();
  },
  methods: {
    loadPlans() {
      subscriptionPlanService.getPlans().then(response => {
        this.plans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadLanguages() {
      subscriptionPlanService.getLanguages().then(response => {
        this.languages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the languages!", error);
      });
    },
    loadModes() {
      subscriptionPlanService.getModes().then(response => {
        this.modes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the modes!", error);
      });
    },
    addPlan() {
      const newPlan = {
        subscription_price: 0,
        subscription_language: this.languages[0]._id,
        subscription_mode: this.modes[0]._id,
        duration_in_months: 0
      };
      this.plans.unshift(newPlan);
      this.editPlanId = newPlan._id;
    },
    editPlan(planId) {
      this.editPlanId = planId;
    },
    savePlan(plan) {
      const planData = {
        ...plan,
        subscription_language: plan.subscription_language,
        subscription_mode: plan.subscription_mode
      };
      if (plan._id) {
        subscriptionPlanService.updatePlan(plan._id, planData).then(() => {
          this.loadPlans();
          this.editPlanId = null;
        }).catch(error => {
          console.error("There was an error updating the subscription plan!", error);
        });
      } else {
        subscriptionPlanService.createPlan(planData).then(() => {
          this.loadPlans();
          this.editPlanId = null;
        }).catch(error => {
          console.error("There was an error creating the subscription plan!", error);
        });
      }
    },
    confirmDeletePlan(planId) {
      this.planToDelete = planId;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    deletePlan() {
      if (this.planToDelete) {
        subscriptionPlanService.deletePlan(this.planToDelete).then(() => {
          this.loadPlans();
          this.hideDeleteModal();
        }).catch(error => {
          console.error("There was an error deleting the subscription plan!", error);
        });
      }
    },
    getLanguageName(languageId) {
      const language = this.languages.find(lang => lang._id === languageId);
      return language ? language.name : '';
    },
    getModeName(modeId) {
      const mode = this.modes.find(m => m._id === modeId);
      return mode ? mode.name : '';
    }
  }
};
</script>

<style scoped>
.table {
  margin-top: 20px;
}
</style>
