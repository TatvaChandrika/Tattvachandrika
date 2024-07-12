<template>
  <div class="container mt-5">
    <h2>Magazine Subscribers</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Magazine Subscribers</li>
      </ol>
    </nav>

    <!-- Add/Edit Subscriber Form -->
    <form @submit.prevent="editMagazineSubscriber ? updateMagazineSubscriber() : addMagazineSubscriber()">
      <div class="mb-3">
        <label for="name">Name</label>
        <input
          type="text"
          id="name"
          v-model="magazineSubscriberForm.name"
          placeholder="Name"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="registration_number">Registration Number</label>
        <input
          type="text"
          id="registration_number"
          v-model="magazineSubscriberForm.registration_number"
          placeholder="Registration Number"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="address">Address</label>
        <input
          type="text"
          id="address"
          v-model="magazineSubscriberForm.address"
          placeholder="Address"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="city_town">City/Town</label>
        <input
          type="text"
          id="city_town"
          v-model="magazineSubscriberForm.city_town"
          placeholder="City/Town"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="state">State</label>
        <input
          type="text"
          id="state"
          v-model="magazineSubscriberForm.state"
          placeholder="State"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="pincode">Pincode</label>
        <input
          type="text"
          id="pincode"
          v-model="magazineSubscriberForm.pincode"
          placeholder="Pincode"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="phone">Phone</label>
        <input
          type="text"
          id="phone"
          v-model="magazineSubscriberForm.phone"
          placeholder="Phone"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="email">Email</label>
        <input
          type="email"
          id="email"
          v-model="magazineSubscriberForm.email"
          placeholder="Email"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="category">Category</label>
        <select id="category" v-model="magazineSubscriberForm.category" class="form-control">
          <option v-for="category in subscriberCategories" :key="category._id" :value="category._id">{{ category.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="stype">Type</label>
        <select id="stype" v-model="magazineSubscriberForm.stype" class="form-control">
          <option v-for="type in subscriberTypes" :key="type._id" :value="type._id">{{ type.name }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="notes">Notes</label>
        <textarea
          id="notes"
          v-model="magazineSubscriberForm.notes"
          placeholder="Notes"
          class="form-control"
        ></textarea>
      </div>
      <div class="mb-3">
        <label for="active">Active</label>
        <input
          type="checkbox"
          id="active"
          v-model="magazineSubscriberForm.active"
          class="form-check-input"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">{{ editMagazineSubscriber ? 'Update' : 'Add' }}</button>
      <button v-if="editMagazineSubscriber" type="button" class="btn btn-secondary mt-2" @click="cancelEdit">Cancel</button>
    </form>

    <!-- Subscribers Table -->
    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Registration Number</th>
          <th>Address</th>
          <th>City/Town</th>
          <th>State</th>
          <th>Pincode</th>
          <th>Phone</th>
          <th>Email</th>
          <th>Category</th>
          <th>Type</th>
          <th>Notes</th>
          <th>Active</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="magazineSubscriber in magazineSubscribers" :key="magazineSubscriber._id">
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.name }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.registration_number }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.address }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.city_town }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.state }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.pincode }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.phone }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.email }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ getCategoryName(magazineSubscriber.category) }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ getTypeName(magazineSubscriber.stype) }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.notes }}</td>
          <td @click="viewSubscriberDetails(magazineSubscriber._id)" style="cursor: pointer;">{{ magazineSubscriber.active ? 'Yes' : 'No' }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="editMagazineSubscriberFunc(magazineSubscriber)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteMagazineSubscriber(magazineSubscriber._id)">Delete</button>
            <router-link :to="{ name: 'AddSubscription', params: { subscriberId: magazineSubscriber._id } }" class="btn btn-info btn-sm">Add Subscription</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import magazineSubscriberService from '../services/magazineSubscriberService';
import subscriberCategoryService from '../services/subscriberCategoryService';
import subscriberTypeService from '../services/subscriberTypeService';

export default {
  data() {
    return {
      magazineSubscribers: [],
      subscriberCategories: [],
      subscriberTypes: [],
      magazineSubscriberForm: {
        name: '',
        registration_number: '',
        address: '',
        city_town: '',
        state: '',
        pincode: '',
        phone: '',
        email: '',
        category: '',
        stype: '',
        notes: '',
        active: true
      },
      editMagazineSubscriber: null
    };
  },
  created() {
    this.loadMagazineSubscribers();
    this.loadSubscriberCategories();
    this.loadSubscriberTypes();
  },
  methods: {
    loadMagazineSubscribers() {
      magazineSubscriberService.getMagazineSubscribers().then(response => {
        this.magazineSubscribers = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the magazine subscribers!", error);
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
    getCategoryName(categoryId) {
      const category = this.subscriberCategories.find(cat => cat._id === categoryId);
      return category ? category.name : 'Unknown';
    },
    getTypeName(typeId) {
      const type = this.subscriberTypes.find(typ => typ._id === typeId);
      return type ? type.name : 'Unknown';
    },
    addMagazineSubscriber() {
      if (this.magazineSubscriberForm.name.trim()) {
        magazineSubscriberService.createMagazineSubscriber(this.magazineSubscriberForm).then(() => {
          this.loadMagazineSubscribers();
          this.resetForm();
        }).catch(error => {
          console.error("There was an error adding the magazine subscriber!", error);
        });
      }
    },
    editMagazineSubscriberFunc(magazineSubscriber) {
      this.editMagazineSubscriber = { ...magazineSubscriber };
      this.magazineSubscriberForm = { ...magazineSubscriber };
    },
    updateMagazineSubscriber() {
      if (this.magazineSubscriberForm.name.trim()) {
        magazineSubscriberService.updateMagazineSubscriber(this.editMagazineSubscriber._id, this.magazineSubscriberForm).then(() => {
          this.loadMagazineSubscribers();
          this.editMagazineSubscriber = null;
          this.resetForm();
        }).catch(error => {
          console.error("There was an error updating the magazine subscriber!", error);
        });
      }
    },
    deleteMagazineSubscriber(id) {
      magazineSubscriberService.deleteMagazineSubscriber(id).then(() => {
        this.loadMagazineSubscribers();
      }).catch(error => {
        console.error("There was an error deleting the magazine subscriber!", error);
      });
    },
    cancelEdit() {
      this.editMagazineSubscriber = null;
      this.resetForm();
    },
    resetForm() {
      this.magazineSubscriberForm = {
        name: '',
        registration_number: '',
        address: '',
        city_town: '',
        state: '',
        pincode: '',
        phone: '',
        email: '',
        category: '',
        stype: '',
        notes: '',
        active: true
      };
    },
    viewSubscriberDetails(subscriberId) {
      this.$router.push({ name: 'SubscriberDetails', params: { subscriberId } });
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>