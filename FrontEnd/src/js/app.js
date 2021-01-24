// Import Vue
import Vue from 'vue';

// Import Framework7
import Framework7 from 'framework7/framework7-lite.esm.bundle.js';

// Import Framework7-Vue Plugin
import Framework7Vue from 'framework7-vue/framework7-vue.esm.bundle.js';
import * as VueGoogleMaps from 'vue2-google-maps'

// Import Framework7 Styles
import 'framework7/css/framework7.bundle.css';

// Import Icons and App Custom Styles
import '../css/icons.css';
import '../css/app.css';

// Import App Component
import App from '../components/app.vue';

// Init Framework7-Vue Plugin
Framework7.use(Framework7Vue);

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDgKTZ2eaI3DHvQm6tkN6Pcq4sLHaEPG8Q',
    libraries: 'places', 
  },
  installComponents: true
})

// Init App
new Vue({
  el: '#app',
  render: (h) => h(App),
  data(){
    return {
      email: '',
      clinicName: '',
      name:'',
      tmpNHS:'',
      sex:'',
      preExisting:[],
      radius:'',
      dob:'',
      phone:'',
    }
  }, 
  // Register App Component
  components: {
    app: App    
  }
});
