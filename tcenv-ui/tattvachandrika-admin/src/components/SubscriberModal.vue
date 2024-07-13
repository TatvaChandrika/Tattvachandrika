<template>
  <div class="modal fade show" tabindex="-1" role="dialog" style="display: block;" v-if="show">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ subscriber ? 'Edit Subscriber' : 'Add Subscriber' }}</h5>
          <button type="button" class="close" @click="close" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="save">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" class="form-control" id="name" v-model="form.name" required>
            </div>
            <div class="form-group">
              <label for="registration_number">Registration Number</label>
              <input type="text" class="form-control" id="registration_number" v-model="form.registration_number" required>
            </div>
            <div class="form-group">
              <label for="city_town">City/Town</label>
              <input type="text" class="form-control" id="city_town" v-model="form.city_town" required>
            </div>
            <div class="form-group">
              <label for="state">State</label>
              <input type="text" class="form-control" id="state" v-model="form.state" required>
            </div>
            <div class="form-group">
              <label for="phone">Phone</label>
              <input type="text" class="form-control" id="phone" v-model="form.phone" required>
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" class="form-control" id="email" v-model="form.email" required>
            </div>
            <div class="form-group">
              <label for="category">Category</label>
              <select class="form-control" id="category" v-model="form.category" required>
                <option v-for="category in categories" :key="category._id" :value="category._id">{{ category.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="stype">Type</label>
              <select class="form-control" id="stype" v-model="form.stype" required>
                <option v-for="stype in types" :key="stype._id" :value="stype._id">{{ stype.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="notes">Notes</label>
              <textarea class="form-control" id="notes" v-model="form.notes"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">{{ subscriber ? 'Save Changes' : 'Add Subscriber' }}</button>
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
    subscriber: Object,
    categories: Array,
    types: Array
  },
  data() {
    return {
      form: {
        name: '',
        registration_number: '',
        city_town: '',
        state: '',
        phone: '',
        email: '',
        category: '',
        stype: '',
        notes: ''
      }
    };
  },
  watch: {
    subscriber: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          this.form = { ...newVal, category: newVal.category._id, stype: newVal.stype._id };
        } else {
          this.form = {
            name: '',
            registration_number: '',
            city_town: '',
            state: '',
            phone: '',
            email: '',
            category: '',
            stype: '',
            notes: ''
          };
        }
      }
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    save() {
      this.$emit('save', { ...this.form });
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
