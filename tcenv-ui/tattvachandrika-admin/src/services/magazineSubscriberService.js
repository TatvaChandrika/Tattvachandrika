import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscribers/';

const getMagazineSubscribers = () => {
  return axios.get(apiUrl);
};

const getMagazineSubscriberById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createMagazineSubscriber = (subscriber) => {
  return axios.post(apiUrl, subscriber);
};

const updateMagazineSubscriber = (id, subscriber) => {
  return axios.put(`${apiUrl}${id}/`, subscriber);
};

const deleteMagazineSubscriber = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getMagazineSubscribers,
  getMagazineSubscriberById,
  createMagazineSubscriber,
  updateMagazineSubscriber,
  deleteMagazineSubscriber
};
