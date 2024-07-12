<template>
  <div class="container mt-5">
    <h2>Subscription Modes</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Modes</li>
      </ol>
    </nav>

    <!-- Add Subscription Mode Form -->
    <form @submit.prevent="addSubscriptionMode">
      <div class="mb-3">
        <input
          type="text"
          v-model="subscriptionModeForm.name"
          placeholder="New Subscription Mode Name"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Add</button>
    </form>

    <!-- Edit Subscription Mode Form (conditional) -->
    <div v-if="editSubscriptionMode">
      <h3>Edit Subscription Mode</h3>
      <form @submit.prevent="updateSubscriptionMode">
        <div class="mb-3">
          <input
            type="text"
            v-model="subscriptionModeForm.name"
            placeholder="Edit Subscription Mode Name"
            class="form-control"
          />
        </div>
        <button type="submit" class="btn btn-success mt-2">Save</button>
        <button type="button" class="btn btn-secondary mt-2" @click="cancelEdit">Cancel</button>
      </form>
    </div>

    <!-- Subscription Modes Table -->
    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subscriptionMode in subscriptionModes" :key="subscriptionMode._id">
          <td>{{ subscriptionMode.name }}</td>
          <td style="border: 10px;">
            <button class="btn btn-warning btn-sm" @click="editMode(subscriptionMode)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteSubscriptionMode(subscriptionMode._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import subscriptionModeService from '../services/subscriptionModeService';

export default {
  data() {
    return {
      subscriptionModes: [],
      subscriptionModeForm: {
        name: ''
      },
      editSubscriptionMode: null
    };
  },
  created() {
    this.loadSubscriptionModes();
  },
  methods: {
    loadSubscriptionModes() {
      subscriptionModeService.getSubscriptionModes().then(response => {
        this.subscriptionModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription modes!", error);
      });
    },
    addSubscriptionMode() {
      if (this.subscriptionModeForm.name.trim()) {
        subscriptionModeService.createSubscriptionMode(this.subscriptionModeForm).then(() => {
          this.loadSubscriptionModes();
          this.subscriptionModeForm.name = '';
        }).catch(error => {
          console.error("There was an error adding the subscription mode!", error);
        });
      }
    },
    editMode(subscriptionMode) {
      this.editSubscriptionMode = { ...subscriptionMode };
      this.subscriptionModeForm.name = subscriptionMode.name;
    },
    updateSubscriptionMode() {
      if (this.subscriptionModeForm.name.trim()) {
        subscriptionModeService.updateSubscriptionMode(this.editSubscriptionMode._id, this.subscriptionModeForm).then(() => {
          this.loadSubscriptionModes();
          this.editSubscriptionMode = null;
          this.subscriptionModeForm.name = '';
        }).catch(error => {
          console.error("There was an error updating the subscription mode!", error);
        });
      }
    },
    deleteSubscriptionMode(id) {
      subscriptionModeService.deleteSubscriptionMode(id).then(() => {
        this.loadSubscriptionModes();
      }).catch(error => {
        console.error("There was an error deleting the subscription mode!", error);
      });
    },
    cancelEdit() {
      this.editSubscriptionMode = null;
      this.subscriptionModeForm.name = '';
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
