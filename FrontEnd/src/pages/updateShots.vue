<template>
  <f7-page name="home">
    <f7-navbar :sliding="false" large>
      <div>
        <f7-button class = "button-fill button" v-on:click="onLogoutClicked" style="text-align:left; width:100%"> Logout </f7-button>
      </div>
      <h4 style="text-align:right; width: 100%;"> <div class="shadow_corner"><img class="logo" src="static/icons/logo.png" /></div></h4>
      <f7-nav-title-large sliding style="text-align:center; width: 100%; color: #005eb8;"> Submit Information </f7-nav-title-large>
    </f7-navbar>
    <h2 style="text-align:center;">Submit SaVaX Alerts For: {{this.clinic}}</h2>
    <h3 style="font-weight: bold;">Enter the number of vaccines remaining in Pfizer and/or Oxford vial:</h3>
    <f7-row>
      <f7-col>
            <f7-input class = "text" style="width:100%; padding:10px" :value="numberOfVaccines" @input="numberOfVaccines = $event.target.value" type="text" placeholder="Enter Number" />
      </f7-col>
      <f7-col>
        <f7-button class = "button button-fill button" v-on:click="updateFinalNum()"> Send Alerts to Users </f7-button>
      </f7-col>
    </f7-row>
    <h3 style="font-weight: bold;">Enter the number of vaccines available due to Pfizer shots expiring tomorrow:</h3>
    <f7-row>
      <f7-col>
            <f7-input class = "text" style="width:100%; padding:10px" :value="numberOfExpired" @input="numberOfExpired = $event.target.value" type="text" placeholder="Enter Number" />
      </f7-col>
      <f7-col>
        <f7-button class = "button button-fill button" v-on:click="updateExpire()"> Send Alerts to Users </f7-button>
      </f7-col>
    </f7-row>
    <span style="display:block; height: 20pt;"></span>
    <div style="border:0.3pt solid black; width:100%; height:0cm"></div>
    <h2 style="text-align:center;">Submit Information of SaVaX Vaccinations</h2>
    <h3 style="font-weight: bold;">Enter the NHS Number of the person vaccinated</h3>
    <f7-row>
      <f7-col>
            <f7-input class = "text" style="width:100%; padding:10px" :value="NHSNumber" @input="NHSNumber = $event.target.value" type="text" placeholder="NHS Number" />
      </f7-col>
      <f7-col>
        <f7-button class = "button button-fill button" v-on:click="updateVax()"> Submit NHS Number </f7-button>
      </f7-col>
    </f7-row>
    <span style="display:block; height: 10pt;"></span>
    <!-- Tabbar for switching views-tabs -->
    <f7-toolbar tabbar labels bottom>
      <f7-link link="#" tab-link-active icon-md="material:done" text="Update"></f7-link>
      <f7-link icon-md="material:info" text="Profile" href="/adminHome/"></f7-link>
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
        numberOfVaccines: 0,
        numberOfExpired: 0,
        NHSNumber: '',
      };
  },
  methods: {
      
      onLogoutClicked() {
        this.$f7.views.main.router.navigate('/login/');
      }, 
      updateFinalNum(){
        console.log(this.numberOfVaccines)
        
        var res = {
            "email": this.email,
            "shotNum": this.numberOfVaccines
        }
        axios.post('/updateFinalShots/', res).then((response)=>{
              // Should just be a boolean - pass/not pass 
              console.log(response.data);
        })
      },
      updateExpire(){
        console.log(this.numberOfExpired)
        
        var res = {
            "email": this.email,
            "shotNum": this.numberOfExpired
        }
        
        axios.post('/updateExpiredShots/', res).then((response)=>{
              // Should just be a boolean - pass/not pass 
              console.log(response.data);
        })
      },
      updateVax(){
        console.log(this.NHSNumber)
        
            date (Month, Day, Year)
        
        // Might not be the right way to get the date for the back-end to parse, but
        // will cross that bridge once there
        var res = {
            "nhs_id": this.NHSNumber,
            "date": new Date().toLocaleDateString("en-US").split("/")
        }
        
        axios.post('/updateNHSVax/', res).then((response)=>{
              // Should just be a boolean - pass/not pass 
              console.log(response.data);
        })
      },
    }, mounted (){
      this.clinic = this.$root.clinicName; 
    }

}
</script>