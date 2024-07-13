import axios from 'axios';

const API_URL = 'http://localhost:8000/api/subscription-plans/';
const LANGUAGES_URL = 'http://localhost:8000/api/subscription-languages/';
const MODES_URL = 'http://localhost:8000/api/subscription-modes/';

export default {
  getPlans() {
    return axios.get(API_URL);
  },
  getPlan(id) {
    return axios.get(`${API_URL}${id}/`);
  },
  createPlan(data) {
    return axios.post(API_URL, data);
  },
  updatePlan(id, data) {
    return axios.put(`${API_URL}${id}/`, data);
  },
  deletePlan(id) {
    return axios.delete(`${API_URL}${id}/`);
  },
  getLanguages() {
    return axios.get(LANGUAGES_URL);
  },
  getModes() {
    return axios.get(MODES_URL);
  }
};
