<template>
  <f7-page name="home">
    <f7-navbar :sliding="false" large>
      <div>
        <f7-button class = "button-fill button" v-on:click="onLogoutClicked" style="text-align:left; width:100%"> Logout </f7-button>
      </div>
      <h4 style="text-align:right; width: 100%;"> {{this.email}}</h4>
      <f7-nav-title-large sliding style="text-align:center; width: 100%;"> Your Info </f7-nav-title-large>
    </f7-navbar>
   
   <f7-block strong>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Email:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.email}}</h3>
      </f7-col>
    </f7-row>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Clinic:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.clinic}}</h3>
      </f7-col>
    </f7-row>
    <f7-row>
      <f7-col>
            <h3 style="text-align:center;">Your Name:</h3>
      </f7-col>
      <f7-col>
        <h3 style="font-weight: normal; text-align:center;">{{this.name}}</h3>
      </f7-col>
    </f7-row>
    </f7-block>
    <h5 style="font-weight: normal;text-align:center; color: #005eb8;"><i>Please contact support@savax.com to change the above fields</i></h5>
    <!-- Tabbar for switching views-tabs -->
    <f7-toolbar tabbar labels bottom>
      <f7-link icon-md="material:done" text="Update" href="/updateShots/"></f7-link>
      <f7-link link="#" tab-link-active icon-md="material:info" text="Profile"></f7-link>
    </f7-toolbar>
  </f7-page>
</template>

<script>
import routes from '../js/routes.js';
//import firebase from 'firebase';
//import 'firebase/auth';
import axios from 'axios'

export default {
  
  data() {
      return {
        email: this.$root.email,
        clinic: 'Aberdeen Travel Health Clinic',
        name: 'John Smith',
        updatedEmail: '',
        updatedClinic: '',
        updatedName: '',
      };
    },
  methods: {
      
      onLogoutClicked() {
        this.$f7.views.main.router.navigate('/login/');
      },
    updateValues(){
      // Make sure they aren't empty and then send them to get updated

      // Perhaps let's not bother test this one

      // Establish it first as the existing data
      var res = {
        "email":this.$root.email,
        "clinicName": this.clinic,
        "fullName": this.fullName
      }
      // Then check for the non-empty entries:
      if(this.updatedEmail!=''){
        res['email']=this.updatedEmail;
      }
      if(this.updatedClinic!=''){
        res['clinicName']=this.updatedClinic;
      }
      if(this.updatedName!=''){
        res['fullName']=this.updatedName;
      }
      axios.post('/updateAdminProfile/', res).then((response)=>{
              console.log(response.data) 
              // Response will just be boolean if it passed
            }) 
      }
    },
    mounted() {
      /*axios.post('/adminProfile/', {
              email: this.email 
            }).then((response)=>{
              this.clinic = response.data.clinicName;
              this.name = response.data.fullName;
            })*/
        this.$root.clinicName = this.clinic; 
    }

}
</script>