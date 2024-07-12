<template>
  <div class="container mt-5">
    <h2>Subscription Plans</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Plans</li>
      </ol>
    </nav>

    <!-- Add Subscription Plan Form -->
    <form @submit.prevent="addSubscriptionPlan">
      <div class="mb-3">
        <label for="version">Version</label>
        <input
          type="text"
          id="version"
          v-model="subscriptionPlanForm.version"
          placeholder="Version"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="name">Name</label>
        <input
          type="text"
          id="name"
          v-model="subscriptionPlanForm.name"
          placeholder="Name"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="start_date">Start Date</label>
        <input
          type="date"
          id="start_date"
          v-model="subscriptionPlanForm.start_date"
          placeholder="Start Date"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="subscription_price">Subscription Price</label>
        <input
          type="number"
          id="subscription_price"
          v-model="subscriptionPlanForm.subscription_price"
          placeholder="Subscription Price"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="subscription_language">Subscription Language</label>
        <select id="subscription_language" v-model="subscriptionPlanForm.subscription_language" class="form-control">
          <option v-for="language in subscriptionLanguages" :key="language._id" :value="language._id">{{ language.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="subscription_mode">Subscription Mode</label>
        <select id="subscription_mode" v-model="subscriptionPlanForm.subscription_mode" class="form-control">
          <option v-for="mode in subscriptionModes" :key="mode._id" :value="mode._id">{{ mode.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="duration_in_months">Duration in Months</label>
        <input
          type="number"
          id="duration_in_months"
          v-model="subscriptionPlanForm.duration_in_months"
          placeholder="Duration in Months"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Add</button>
    </form>

    <!-- Edit Subscription Plan Form (conditional) -->
    <div v-if="editSubscriptionPlan">
      <h3>Edit Subscription Plan</h3>
      <form @submit.prevent="updateSubscriptionPlan">
        <div class="mb-3">
          <label for="version">Version</label>
          <input
            type="text"
            id="version"
            v-model="subscriptionPlanForm.version"
            placeholder="Version"
            class="form-control"
          />
        </div>
        <div class="mb-3">
          <label for="name">Name</label>
          <input
            type="text"
            id="name"
            v-model="subscriptionPlanForm.name"
            placeholder="Name"
            class="form-control"
          />
        </div>
        <div class="mb-3">
          <label for="start_date">Start Date</label>
          <input
            type="date"
            id="start_date"
            v-model="subscriptionPlanForm.start_date"
            placeholder="Start Date"
            class="form-control"
          />
        </div>
        <div class="mb-3">
          <label for="subscription_price">Subscription Price</label>
          <input
            type="number"
            id="subscription_price"
            v-model="subscriptionPlanForm.subscription_price"
            placeholder="Subscription Price"
            class="form-control"
          />
        </div>
        <div class="mb-3">
          <label for="subscription_language">Subscription Language</label>
          <select id="subscription_language" v-model="subscriptionPlanForm.subscription_language" class="form-control">
            <option v-for="language in subscriptionLanguages" :key="language._id" :value="language._id">{{ language.name }}</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="subscription_mode">Subscription Mode</label>
          <select id="subscription_mode" v-model="subscriptionPlanForm.subscription_mode" class="form-control">
            <option v-for="mode in subscriptionModes" :key="mode._id" :value="mode._id">{{ mode.name }}</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="duration_in_months">Duration in Months</label>
          <input
            type="number"
            id="duration_in_months"
            v-model="subscriptionPlanForm.duration_in_months"
            placeholder="Duration in Months"
            class="form-control"
          />
        </div>
        <button type="submit" class="btn btn-success mt-2">Save</button>
        <button type="button" class="btn btn-secondary mt-2" @click="cancelEdit">Cancel</button>
      </form>
    </div>

    <!-- Subscription Plans Table -->
    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Version</th>
          <th>Name</th>
          <th>Start Date</th>
          <th>Subscription Price</th>
          <th>Language</th>
          <th>Mode</th>
          <th>Duration</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subscriptionPlan in subscriptionPlans" :key="subscriptionPlan._id">
          <td>{{ subscriptionPlan.version }}</td>
          <td>{{ subscriptionPlan.name }}</td>
          <td>{{ subscriptionPlan.start_date }}</td>
          <td>{{ subscriptionPlan.subscription_price }}</td>
          <td>{{ getLanguageName(subscriptionPlan.subscription_language) }}</td>
          <td>{{ getModeName(subscriptionPlan.subscription_mode) }}</td>
          <td>{{ subscriptionPlan.duration_in_months }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="editPlan(subscriptionPlan)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteSubscriptionPlan(subscriptionPlan._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import subscriptionPlanService from '../services/subscriptionPlanService';
import subscriptionLanguageService from '../services/subscriptionLanguageService';
import subscriptionModeService from '../services/subscriptionModeService';

export default {
  data() {
    return {
      subscriptionPlans: [],
      subscriptionLanguages: [],
      subscriptionModes: [],
      subscriptionPlanForm: {
        version: '',
        name: '',
        start_date: '',
        subscription_price: 0,
        subscription_language: '',
        subscription_mode: '',
        duration_in_months: 0
      },
      editSubscriptionPlan: null
    };
  },
  created() {
    this.loadSubscriptionPlans();
    this.loadSubscriptionLanguages();
    this.loadSubscriptionModes();
  },
  methods: {
    loadSubscriptionPlans() {
      subscriptionPlanService.getSubscriptionPlans().then(response => {
        this.subscriptionPlans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadSubscriptionLanguages() {
      subscriptionLanguageService.getSubscriptionLanguages().then(response => {
        this.subscriptionLanguages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription languages!", error);
      });
    },
    loadSubscriptionModes() {
      subscriptionModeService.getSubscriptionModes().then(response => {
        this.subscriptionModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription modes!", error);
      });
    },
    getLanguageName(languageId) {
      const language = this.subscriptionLanguages.find(lang => lang._id === languageId);
      return language ? language.name : 'Unknown';
    },
    getModeName(modeId) {
      const mode = this.subscriptionModes.find(mode => mode._id === modeId);
      return mode ? mode.name : 'Unknown';
    },
    addSubscriptionPlan() {
      if (this.subscriptionPlanForm.name.trim()) {
        const form = {
          ...this.subscriptionPlanForm,
          subscription_language: this.subscriptionPlanForm.subscription_language,
          subscription_mode: this.subscriptionPlanForm.subscription_mode,
        };
        subscriptionPlanService.createSubscriptionPlan(form).then(() => {
          this.loadSubscriptionPlans();
          this.resetForm();
        }).catch(error => {
          console.error("There was an error adding the subscription plan!", error);
        });
      }
    },
    editPlan(subscriptionPlan) {
      this.editSubscriptionPlan = { ...subscriptionPlan };
      this.subscriptionPlanForm = { 
        ...subscriptionPlan, 
        subscription_language: subscriptionPlan.subscription_language,
        subscription_mode: subscriptionPlan.subscription_mode 
      };
    },
    updateSubscriptionPlan() {
      if (this.subscriptionPlanForm.name.trim()) {
        const form = {
          ...this.subscriptionPlanForm,
          subscription_language: this.subscriptionPlanForm.subscription_language,
          subscription_mode: this.subscriptionPlanForm.subscription_mode,
        };
        subscriptionPlanService.updateSubscriptionPlan(this.editSubscriptionPlan._id, form).then(() => {
          this.loadSubscriptionPlans();
          this.editSubscriptionPlan = null;
          this.resetForm();
        }).catch(error => {
          console.error("There was an error updating the subscription plan!", error);
        });
      }
    },
    deleteSubscriptionPlan(id) {
      subscriptionPlanService.deleteSubscriptionPlan(id).then(() => {
        this.loadSubscriptionPlans();
      }).catch(error => {
        console.error("There was an error deleting the subscription plan!", error);
      });
    },
    cancelEdit() {
      this.editSubscriptionPlan = null;
      this.resetForm();
    },
    resetForm() {
      this.subscriptionPlanForm = {
        version: '',
        name: '',
        start_date: '',
        subscription_price: 0,
        subscription_language: '',
        subscription_mode: '',
        duration_in_months: 0
      };
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
