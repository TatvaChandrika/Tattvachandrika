<template>
  <div class="modal" :class="{ 'is-active': show }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ plan._id ? 'Edit' : 'Add' }} Subscription Plan</p>
        <button class="delete" aria-label="close" @click="$emit('close')"></button>
      </header>
      <section class="modal-card-body">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input class="input" type="text" v-model="localPlan.name" readonly />
          </div>
        </div>
        <div class="field">
          <label class="label">Version</label>
          <div class="control">
            <input class="input" type="text" v-model="localPlan.version" readonly />
          </div>
        </div>
        <div class="field">
          <label class="label">Start Date</label>
          <div class="control">
            <input class="input" type="date" v-model="localPlan.start_date" />
          </div>
        </div>
        <div class="field">
          <label class="label">Price</label>
          <div class="control">
            <input class="input" type="number" v-model="localPlan.subscription_price" />
          </div>
        </div>
        <div class="field">
          <label class="label">Language</label>
          <div class="control">
            <div class="select">
              <select v-model="localPlan.subscription_language">
                <option v-for="language in languages" :key="language._id" :value="language._id">{{ language.name }}</option>
              </select>
            </div>
          </div>
        </div>
        <div class="field">
          <label class="label">Mode</label>
          <div class="control">
            <div class="select">
              <select v-model="localPlan.subscription_mode">
                <option v-for="mode in modes" :key="mode._id" :value="mode._id">{{ mode.name }}</option>
              </select>
            </div>
          </div>
        </div>
        <div class="field">
          <label class="label">Duration (Months)</label>
          <div class="control">
            <input class="input" type="number" v-model="localPlan.duration_in_months" />
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">Save</button>
        <button class="button" @click="$emit('close')">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    plan: Object,
    languages: Array,
    modes: Array
  },
  data() {
    return {
      localPlan: { ...this.plan }
    };
  },
  watch: {
    plan(newPlan) {
      this.localPlan = { ...newPlan };
    }
  },
  methods: {
    save() {
      this.$emit('save', this.localPlan);
    }
  }
};
</script>

<style scoped>
.modal-card {
  width: 100%;
  max-width: 640px;
}
</style>
