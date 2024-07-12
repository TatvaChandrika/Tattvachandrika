<template>
  <div class="container mt-5">
    <h2>Subscription Languages</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Languages</li>
      </ol>
    </nav>

    <!-- Add Subscription Language Form -->
    <form @submit.prevent="addSubscriptionLanguage">
      <div class="mb-3">
        <input
          type="text"
          v-model="subscriptionLanguageForm.name"
          placeholder="New Subscription Language Name"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Add</button>
    </form>

    <!-- Edit Subscription Language Form (conditional) -->
    <div v-if="editSubscriptionLanguage">
      <h3>Edit Subscription Language</h3>
      <form @submit.prevent="updateSubscriptionLanguage">
        <div class="mb-3">
          <input
            type="text"
            v-model="subscriptionLanguageForm.name"
            placeholder="Edit Subscription Language Name"
            class="form-control"
          />
        </div>
        <button type="submit" class="btn btn-success mt-2">Save</button>
        <button type="button" class="btn btn-secondary mt-2" @click="cancelEdit">Cancel</button>
      </form>
    </div>

    <!-- Subscription Languages Table -->
    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subscriptionLanguage in subscriptionLanguages" :key="subscriptionLanguage._id">
          <td>{{ subscriptionLanguage.name }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="editLanguage(subscriptionLanguage)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteSubscriptionLanguage(subscriptionLanguage._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import subscriptionLanguageService from '../services/subscriptionLanguageService';

export default {
  data() {
    return {
      subscriptionLanguages: [],
      subscriptionLanguageForm: {
        name: ''
      },
      editSubscriptionLanguage: null
    };
  },
  created() {
    this.loadSubscriptionLanguages();
  },
  methods: {
    loadSubscriptionLanguages() {
      subscriptionLanguageService.getSubscriptionLanguages().then(response => {
        this.subscriptionLanguages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription languages!", error);
      });
    },
    addSubscriptionLanguage() {
      if (this.subscriptionLanguageForm.name.trim()) {
        subscriptionLanguageService.createSubscriptionLanguage(this.subscriptionLanguageForm).then(() => {
          this.loadSubscriptionLanguages();
          this.subscriptionLanguageForm.name = '';
        }).catch(error => {
          console.error("There was an error adding the subscription language!", error);
        });
      }
    },
    editLanguage(subscriptionLanguage) {
      this.editSubscriptionLanguage = { ...subscriptionLanguage };
      this.subscriptionLanguageForm.name = subscriptionLanguage.name;
    },
    updateSubscriptionLanguage() {
      if (this.subscriptionLanguageForm.name.trim()) {
        subscriptionLanguageService.updateSubscriptionLanguage(this.editSubscriptionLanguage._id, this.subscriptionLanguageForm).then(() => {
          this.loadSubscriptionLanguages();
          this.editSubscriptionLanguage = null;
          this.subscriptionLanguageForm.name = '';
        }).catch(error => {
          console.error("There was an error updating the subscription language!", error);
        });
      }
    },
    deleteSubscriptionLanguage(id) {
      subscriptionLanguageService.deleteSubscriptionLanguage(id).then(() => {
        this.loadSubscriptionLanguages();
      }).catch(error => {
        console.error("There was an error deleting the subscription language!", error);
      });
    },
    cancelEdit() {
      this.editSubscriptionLanguage = null;
      this.subscriptionLanguageForm.name = '';
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
