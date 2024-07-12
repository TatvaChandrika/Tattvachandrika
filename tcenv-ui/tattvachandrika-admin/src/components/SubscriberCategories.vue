<template>
  <div class="container mt-5">
    <h2>Subscriber Categories</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscriber Categories</li>
      </ol>
    </nav>

    <!-- Add Subscriber Category Form -->
    <form @submit.prevent="addSubscriberCategory">
      <div class="mb-3">
        <input
          type="text"
          v-model="subscriberCategoryForm.name"
          placeholder="New Subscriber Category Name"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Add</button>
    </form>

    <!-- Edit Subscriber Category Form (conditional) -->
    <div v-if="editSubscriberCategory">
      <h3>Edit Subscriber Category</h3>
      <form @submit.prevent="updateSubscriberCategory">
        <div class="mb-3">
          <input
            type="text"
            v-model="subscriberCategoryForm.name"
            placeholder="Edit Subscriber Category Name"
            class="form-control"
          />
        </div>
        <button type="submit" class="btn btn-success mt-2">Save</button>
        <button type="button" class="btn btn-secondary mt-2" @click="cancelEdit">Cancel</button>
      </form>
    </div>

    <!-- Subscriber Categories Table -->
    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subscriberCategory in subscriberCategories" :key="subscriberCategory._id">
          <td>{{ subscriberCategory.name }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="editCategory(subscriberCategory)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteSubscriberCategory(subscriberCategory._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import subscriberCategoryService from '../services/subscriberCategoryService';

export default {
  data() {
    return {
      subscriberCategories: [],
      subscriberCategoryForm: {
        name: ''
      },
      editSubscriberCategory: null
    };
  },
  created() {
    this.loadSubscriberCategories();
  },
  methods: {
    loadSubscriberCategories() {
      subscriberCategoryService.getSubscriberCategories().then(response => {
        this.subscriberCategories = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber categories!", error);
      });
    },
    addSubscriberCategory() {
      if (this.subscriberCategoryForm.name.trim()) {
        subscriberCategoryService.createSubscriberCategory(this.subscriberCategoryForm).then(() => {
          this.loadSubscriberCategories();
          this.subscriberCategoryForm.name = '';
        }).catch(error => {
          console.error("There was an error adding the subscriber category!", error);
        });
      }
    },
    editCategory(subscriberCategory) {
      this.editSubscriberCategory = { ...subscriberCategory };
      this.subscriberCategoryForm.name = subscriberCategory.name;
    },
    updateSubscriberCategory() {
      if (this.subscriberCategoryForm.name.trim()) {
        subscriberCategoryService.updateSubscriberCategory(this.editSubscriberCategory._id, this.subscriberCategoryForm).then(() => {
          this.loadSubscriberCategories();
          this.editSubscriberCategory = null;
          this.subscriberCategoryForm.name = '';
        }).catch(error => {
          console.error("There was an error updating the subscriber category!", error);
        });
      }
    },
    deleteSubscriberCategory(id) {
      subscriberCategoryService.deleteSubscriberCategory(id).then(() => {
        this.loadSubscriberCategories();
      }).catch(error => {
        console.error("There was an error deleting the subscriber category!", error);
      });
    },
    cancelEdit() {
      this.editSubscriberCategory = null;
      this.subscriberCategoryForm.name = '';
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
