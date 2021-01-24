<template>
  <f7-page name="home">
  <!-- Top Navbar -->
    <f7-navbar :sliding="false" large>
      <div>
        <f7-button class = "button-fill button" v-on:click="goBack()" style="text-align:left; width:100%"> Go Back </f7-button>
      </div>
      <h4 style="text-align:right; width: 100%;"> <div class="shadow_corner"><img class="logo" src="static/icons/logo.png" /></div></h4>
      <f7-nav-title-large sliding style="text-align:center; width: 100%; color: #005eb8;"> User Registration </f7-nav-title-large>
    </f7-navbar>

  <!-- Page content-->
  <!-- OLD BIGGER SPACE<f7-block strong> -->
  <f7-block>
    <form @submit.prevent="onSignupClicked" action="">
      <f7-list class = "login-list" no-hairlines-md>
        <f7-list-input class="email-input" :value="name" @input="name = $event.target.value" label="Enter your name"  placeholder="John Smith" />
        <f7-list-input large class="username-input" :value="tmpNHS" @input="tmpNHS = $event.target.value" label = "Enter your NHS Number" placeholder="NHS Number" />
        <!--<f7-list-input  type="datepicker" label = "Enter your Date of Birth" placeholder="Select Date Of Birth"
  :calendar-params="{dateFormat: { month: 'long', day: '2-digit', year: 'numeric' }}" :value="dob" @calendar:change="(value) => inputBeginTime = value" />-->
        <f7-list-item class = "smart-select"   title="Choose Gender"> 
          <select v-model="sex">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
        </f7-list-item>
        <f7-list-input :value="radius" @input="radius = $event.target.value" label="Enter your desired alert radius" placeholder="(10 km)" />
        <f7-list-input :value="phone" @input="phone = $event.target.value" label="Enter your phone number" placeholder="+44 XXXX XXXXXX" />
        <f7-list-input class="email-input" :value="email" @input="email = $event.target.value" label="Type in your email address" type="email" placeholder="E-mail" />
        
        <f7-list-input :value="password" @input="password = $event.target.value" label="Choose a password" type ="password" placeholder="Password" />
      </f7-list-item>
      </f7-list>

      <f7-list>
        <div style="border:0.3pt solid black; width:100%; height:0cm"></div>
        <f7-list-item title = "Autofill your address">
          <f7-button class = "button button-fill button" label = "Auto fill for your current address" v-on:click="getAddress()"> Get address </f7-button>
        </f7-list-item>
        <f7-list-item>
          Address: {{this.lat}}, {{this.lng}}
        </f7-list-item>
      </f7-list>

      <!--<h5 style="font-weight: normal;text-align:left; color: #C0C0C0;">Click to Autofill Current Address</h5> -->      

      <div style="border:0.3pt solid black; width:100%; height:0cm"></div>
      <h5 style="font-weight: normal;text-align:center; color: #005eb8;"><i>If you have (or have had) any of the following, you are currently unable to book any vaccinations via the SaVaX app</i></h5>
      <f7-list>
      <f7-list-item class = "smart-select" title="Do you have any of the following?"> 
          <select v-model="preExisting" multiple>
            <option value="Condition 1">Require Immunosuppression</option>
            <option value="Condition 2">Autoimmune Disease</option>
            <option value="Condition 3">History of Guillain-Barre Syndrome</option>
            <option value="Condition 4">History of Bell's Palsy</option>
            <option value="Condition 5">History of Dermal Filler Use</option>
            <option value="Condition 6">Pregnant or lactating</option>
          </select>
        </f7-list-item>
      </f7-list>
      <f7-button fill type ="submit"> Sign up </f7-button>
    </form>
  </f7-block>
  </f7-page>

</template>

<script> 
  import routes from '../js/routes.js';
  import axios from 'axios'

  export default{

    data() {
      
      return {
        email: '',
        name: '',
        tmpNHS: '',
        password: '',
        phone: '',
        sex: '',
        radius: '',
        preExisting: [],
        lat: 0,
        lng: 0,
        dob: [],
        loggedOn: true, // can set to true when testing
      };
    },
    methods: {
      goBack() {
        this.$f7.views.main.router.navigate('/login/');
      },
      onSignupClicked(e){
        var res = {
          "name":this.name,
          "nhs_id":this.tmpNHS,
          "sex":this.sex,
          "conditions":this.preExisting,
          "location":[this.lat,this.lng],
          "radius": this.radius,
          //"DOB": this.dob,
          "Phone": this.phone,
          "email": this.email,
          "password": this.password
        };
        this.$root.name = this.name;
        this.$root.tmpNHS = this.tmpNHS;
        this.$root.sex = this.sex;
        this.$root.preExisting = this.preExisting;
        this.$root.radius = this.radius;
        //this.$root.dob = this.dob;
        this.$root.phone = this.phone;
        console.log(res);
        /*axios.post('/userReg/', {res}).then((response)=>{
              console.log(response.data);
              this.loggedOn = response.data.response;  
          })*/
        if(this.loggedOn){
          this.$root.email = this.email;
          this.$f7.views.main.router.navigate('/userHome/');
        }
      },
      getAddress() {
        navigator.geolocation.getCurrentPosition(
              position => {
              this.lat = position.coords.latitude;
              this.lng = position.coords.longitude;
            },
            error => {
              console.log(error.message);
            },
          )
      }
    }
  };

</script>