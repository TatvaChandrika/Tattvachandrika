import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscriptions/';

const getSubscriptions = () => {
  return axios.get(apiUrl);
};

const getSubscriptionById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const getSubscriptionsBySubscriberId = (subscriberId) => {
  return axios.get(`${apiUrl}?subscriber=${subscriberId}`);
};

const createSubscription = (subscription) => {
  return axios.post(apiUrl, subscription);
};

const updateSubscription = (id, subscription) => {
  return axios.put(`${apiUrl}${id}/`, subscription);
};

const deleteSubscription = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getSubscriptions,
  getSubscriptionById,
  getSubscriptionsBySubscriberId,
  createSubscription,
  updateSubscription,
  deleteSubscription
};
