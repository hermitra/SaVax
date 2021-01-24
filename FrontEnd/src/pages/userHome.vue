<template>
  <f7-page name="home">
    <f7-navbar :sliding="false" large>
      <div>
        <f7-button class = "button-fill button" v-on:click="onLogoutClicked" style="text-align:left; width:100%"> Logout </f7-button>
      </div>
      <h4 style="text-align:right; width: 100%;"> {{this.email}}</h4>
      <div class="shadow"><img class="logo" src="static/icons/logo.png" /></div>
    </f7-navbar>
    
    <GmapMap ref="mapRef"
    :center="{lat:this.lat, lng:this.lng}"
    :zoom="12"
    map-type-id="terrain"
    style="width: 500px; height: 50%"
    :options="{
    zoomControl: true,
    mapTypeControl: false,
    scaleControl: false,
    streetViewControl: false,
    rotateControl: false,
    fullscreenControl: true,
    disableDefaultUI: true
    }">
    <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m"
        @click="center=m"
      ></gmap-marker>

    </GmapMap> 
    
    <f7-block>
       <f7-block-title style="text-align: center; font-size:large" > {{this.Clinics.length}} Clinics: </f7-block-title>
       <f7-list no-hairlines-md>
         <f7-row>
           <f7-col> <p class = "text-align-center" style="font-size:large"> Clinic's Name </p> </f7-col> 
           <f7-col> <p class = "text-align-center" style="font-size:large"> Location </p> </f7-col> 
           <f7-col> <p class = "text-align-center" style="font-size:large"> Remaining Shots </p> </f7-col> 
         </f7-row>
         <f7-list-item v-for="clinic in Clinics" :key="clinic.label"> 
           <f7-col> <p class = "text-align-center" style="font-size:large"> {{ clinic.label }} </p> </f7-col> 
           <f7-col> <p class = "text-align-center" style="font-size:large"> {{clinic.Location}} </p> </f7-col> 
           <f7-col> <p class = "text-align-center" style="font-size:large"> {{clinic.Shots}} </p> </f7-col> </f7-list-item>
       </f7-list>
    </f7-block>
    
    <!-- Tabbar for switching views-tabs -->
    <f7-toolbar tabbar labels bottom>
      <f7-link link="#" tab-link-active icon-md="material:home" text="Centres"></f7-link>
      <f7-link icon-md="material:info" text="Profile" href="/userProfile/"></f7-link>
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
        lat: 0,
        lng: 0,
        Clinics: [
          {"label":"Marywell Healthcare Centre","Location":[57.143780, -2.100320], "Shots":3},
          {"label":"Aberdeen Royal Infirmary","Location":[57.153970,  -2.131780], "Shots":4},
          {"label":"Carden Medical Centre","Location":[57.145480, -2.115800], "Shots":2},
          {"label":"Royal Cornhill Hospital","Location":[57.156150, -2.126570], "Shots":1},
          {"label":"Royal Aberdeen Children's Hospital","Location":[57.152380, -2.131740], "Shots":3},
        ],
        markers: [],
        nhs: [],
        location: null,
        // When locate nearest center is clicked,
        // the lat, lng will be stored in nearestCenter
        nearestCenter: null
      };
    },
  methods: {
      
      onLogoutClicked() {
        this.$f7.views.main.router.navigate('/login/');
      }, 
      setMarker(Points, Label){
        const markers = new google.maps.Marker({
          position:Points,
          map:this.map,
          label:{
            text:Label,
            color:"#FFF"
          }
        })
      }
      /** When interacting with the back-end, this is a template of how that might work:
       axios.post('http://127.0.0.1:5000/parse/', {
              email: this.email, 
              NHS: this.NHS,
              location: this.location
            }).then((response)=>{
              console.log(response.data);  
            }) */
    },
    mounted () {
    navigator.geolocation.getCurrentPosition(
              position => {
              this.lat = position.coords.latitude;
              this.lng = position.coords.longitude;
            },
            error => {
              console.log(error.message);
            },
    )
    this.markers = [{lat:57.143780, lng:-2.100320, label:"Marywell Healthcare Centre"},
          {lat:57.153970,  lng: -2.131780, "label":"Aberdeen Royal Infirmary"},
          {lat:57.145480, lng:-2.115800, "label":"Carden Medical Centre"},
          {lat:57.156150, lng: -2.126570, label:"Royal Cornhill Hospital"},
          {lat:57.152380, lng: -2.131740, label:"Royal Aberdeen Children's Hospital"},]
    // Can replace lat lng with closest center
    this.$refs.mapRef.$mapPromise.then((map) => {
      map.panTo({lat:this.lat, lng:this.lng})
    })
  }
}
</script>