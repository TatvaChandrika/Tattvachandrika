import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscription-plans/'; // Adjust the URL to your API endpoint

const getSubscriptionPlans = () => {
  return axios.get(apiUrl);
};

const getSubscriptionPlanById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createSubscriptionPlan = (subscriptionPlan) => {
  return axios.post(apiUrl, subscriptionPlan);
};

const updateSubscriptionPlan = (id, subscriptionPlan) => {
  return axios.put(`${apiUrl}${id}/`, subscriptionPlan);
};

const deleteSubscriptionPlan = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getSubscriptionPlans,
  getSubscriptionPlanById,
  createSubscriptionPlan,
  updateSubscriptionPlan,
  deleteSubscriptionPlan
};
