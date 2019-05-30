import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';
import {ServerTable, Event} from 'vue-tables-2';
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
 

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import routes from './routes'

const router = new VueRouter({
  mode: 'history',
  routes
})

axios.defaults.baseURL = 'http://localhost:3000';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*'

Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(BootstrapVue);
Vue.use(ServerTable, {}, false, 'bootstrap4');

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
