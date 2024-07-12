<template>
  <div class="container mt-5">
    <h2>Subscriber Types</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscriber Types</li>
      </ol>
    </nav>

    <!-- Add Subscriber Type Form -->
    <form @submit.prevent="addSubscriberType">
      <div class="mb-3">
        <input
          type="text"
          v-model="subscriberTypeForm.name"
          placeholder="New Subscriber Type Name"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Add</button>
    </form>

    <!-- Edit Subscriber Type Form (conditional) -->
    <div v-if="editSubscriberType">
      <h3>Edit Subscriber Type</h3>
      <form @submit.prevent="updateSubscriberType">
        <div class="mb-3">
          <input
            type="text"
            v-model="subscriberTypeForm.name"
            placeholder="Edit Subscriber Type Name"
            class="form-control"
          />
        </div>
        <button type="submit" class="btn btn-success mt-2">Save</button>
        <button type="button" class="btn btn-secondary mt-2" @click="cancelEdit">Cancel</button>
      </form>
    </div>

    <!-- Subscriber Types Table -->
    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subscriberType in subscriberTypes" :key="subscriberType._id">
          <td>{{ subscriberType.name }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="editType(subscriberType)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteSubscriberType(subscriberType._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import subscriberTypeService from '../services/subscriberTypeService';

export default {
  data() {
    return {
      subscriberTypes: [],
      subscriberTypeForm: {
        name: ''
      },
      editSubscriberType: null
    };
  },
  created() {
    this.loadSubscriberTypes();
  },
  methods: {
    loadSubscriberTypes() {
      subscriberTypeService.getSubscriberTypes().then(response => {
        this.subscriberTypes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber types!", error);
      });
    },
    addSubscriberType() {
      if (this.subscriberTypeForm.name.trim()) {
        subscriberTypeService.createSubscriberType(this.subscriberTypeForm).then(() => {
          this.loadSubscriberTypes();
          this.subscriberTypeForm.name = '';
        }).catch(error => {
          console.error("There was an error adding the subscriber type!", error);
        });
      }
    },
    editType(subscriberType) {
      this.editSubscriberType = { ...subscriberType };
      this.subscriberTypeForm.name = subscriberType.name;
    },
    updateSubscriberType() {
      if (this.subscriberTypeForm.name.trim()) {
        subscriberTypeService.updateSubscriberType(this.editSubscriberType._id, this.subscriberTypeForm).then(() => {
          this.loadSubscriberTypes();
          this.editSubscriberType = null;
          this.subscriberTypeForm.name = '';
        }).catch(error => {
          console.error("There was an error updating the subscriber type!", error);
        });
      }
    },
    deleteSubscriberType(id) {
      subscriberTypeService.deleteSubscriberType(id).then(() => {
        this.loadSubscriberTypes();
      }).catch(error => {
        console.error("There was an error deleting the subscriber type!", error);
      });
    },
    cancelEdit() {
      this.editSubscriberType = null;
      this.subscriberTypeForm.name = '';
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
