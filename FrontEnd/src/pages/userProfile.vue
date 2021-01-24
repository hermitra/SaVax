<template>
  <f7-page name="home">
    <f7-navbar :sliding="false" large>
      <div>
        <f7-button class = "button-fill button" v-on:click="onLogoutClicked" style="text-align:left; width:100%"> Logout </f7-button>
      </div>
      <h4 style="text-align:right; width: 100%;"> <div class="shadow_corner"><img class="logo" src="static/icons/logo.png" /></div></h4>
      <f7-nav-title-large sliding style="text-align:center; width: 100%; color: #005eb8;"> Your Profile </f7-nav-title-large>
      <!--Administrative, wasn't fitting the whole phrase on my display-->
    </f7-navbar>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Name:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.name}}</h3>
      </f7-col>
    </f7-row>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your NHS Number:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.tmpNHS}}</h3>
      </f7-col>
    </f7-row>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Sex:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.sex}}</h3>
      </f7-col>
    </f7-row>
    <f7-row>
      <!--<f7-col>
            <h3 style="text-align:center;">Your D.o.B:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.dob}}</h3>
      </f7-col>-->
    </f7-row>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Phone Number:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.phone}}</h3>
      </f7-col>
    </f7-row>
    <h5 style="font-weight: normal;text-align:center; color: #005eb8;"><i>Please contact support@savax.com to change the above fields</i></h5>
    <div style="border:0.3pt solid black; width:100%; height:0cm"></div>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Search Radius:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.radius}}</h3>
      </f7-col>
    </f7-row>

    <h3 style="font-weight: normal;">Enter Your New Search Radius:</h3>
    <f7-row>
      <f7-col>
            <f7-input class = "text" style="width:100%; padding:10px" :value="radius" @input="radius = $event.target.value" type="text" placeholder="Enter Number" />
      </f7-col>
      <f7-col>
        <f7-button class = "button button-fill button" v-on:click="updateSearchRadius()"> Click to Search Radius </f7-button>
      </f7-col>
    </f7-row>

    <span style="display:block; height: 10pt;"></span>

    <!-- Tabbar for switching views-tabs -->
    <f7-toolbar tabbar labels bottom>
      <f7-link icon-md="material:home" text="Centres" href="/userHome/"></f7-link>
      <f7-link link="#" tab-link-active icon-md="material:info" text="Profile"></f7-link>
    </f7-toolbar>
  </f7-page>
</template>

<script>
import routes from '../js/routes.js';
import axios from 'axios'

export default {
  
   data() {
      return {
        email: this.$root.email,
        clinic: '',
        name: '',
        radius: '',
        tmpNHS: '',
        sex: '',
        dob: '',
        phone: '',
      };
  },
  methods: {
      
      onLogoutClicked() {
        this.$f7.views.main.router.navigate('/login/');
      }, 
      updateSearchRadius(){
        console.log(this.radius)
        //axios post the number
      },
      /** When interacting with the back-end, this is a template of how that might work:
       axios.post('http://127.0.0.1:5000/parse/', {
              email: this.email, 
              NHS: this.NHS,
              location: this.location
            }).then((response)=>{
              console.log(response.data);  
            }) */
    }, mounted (){
      this.clinic = 'Aberdeen Travel Health Clinic'; // Will be filled in with login
      this.name = this.$root.name; // Will be filled in with login
      this.tmpNHS = this.$root.tmpNHS; // Will be filled in with login
      this.sex = this.$root.sex; // Will be filled in with login
      this.radius = this.$root.radius; // Will be filled in with login
      this.dob = this.$root.dob; // Will be filled in with login
      this.phone = this.$root.phone; // Will be filled in with login 
      
    }

}
</script>