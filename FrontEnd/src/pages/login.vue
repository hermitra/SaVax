<template>
  <f7-page name="home">
  <!-- Top Navbar -->
    <f7-navbar :sliding="false" large>
      <div class="shadow"><img class="logo" src="static/icons/logo.png" /></div>

    </f7-navbar>

  <!-- Page content-->
  <f7-block v-if="user" strong>
    <f7-block-header> You are logged in as {{user.displayName}} {{user.email}} </f7-block-header>
    <f7-button v-on:click="onLogoutClicked"> Logout </f7-button>
  </f7-block>
  <f7-block v-else strong>
    <form @submit.prevent="onLoginWithEmailClicked" action="" method="GET">
    <f7-list class = "login-list" no-hairlines-md>
      <f7-list-input class = "email-input" :value="email" @input="email = $event.target.value" label="Login with your email address" type="email" placeholder="Email Address" />
      <f7-list-input :value="password" @input="password = $event.target.value" label="Provide your password" type="password" placeholder="Password" />
    </f7-list>
    <f7-button fill type ="submit"> Login </f7-button>
    </form>
  </f7-block>

  <f7-block v-if="!user" strong>
    <f7-block-title> No account yet? </f7-block-title>
    <f7-button v-if="!showSignupForm" fill v-on:click="showSignupForm = true"> Create new account </f7-button>
    <f7-row v-if="showSignupForm">
      <f7-col>
        <f7-button class = "button button-fill button" v-on:click="toUserReg()"> User Registration </f7-button>
      </f7-col>
      <f7-col>
        <f7-button class = "button button-fill button" v-on:click="toAdminReg()"> Admin Registration </f7-button>
      </f7-col>
    </f7-row>
  </f7-block>
  
  </f7-page>

</template>

<script> 
  import routes from '../js/routes.js';
  import axios from 'axios'

  export default{

    data() {
      
      return {
        user: null,
        email: '', 
        NHS: '',
        lat: 0,
        lng: 0,
        password: '',
        isAdmin: true, 
        loggedOn: true,
        showSignupForm: false,
      };
    },
    methods: {
      goBack() {
        this.$f7.loginScreen.close();
      },
      onLoginWithEmailClicked() {
        var res = {
            "email": this.email,
            "password": this.password,
            "location": {
              "lat": this.lat,
              "lng": this.lng
            }
        }
        /*axios.post('/adminReg/', res).then((response)=>{
              this.loggedOn = response.data.response;
              this.isAdmin = response.data.isAdmin
        })*/ 
        if(this.loggedOn){
          this.$root.email = this.email;
          if(this.isAdmin){
            this.$root.email = this.email;
            this.$f7.views.main.router.navigate('/adminHome/');
          } else{ 
            this.$f7.views.main.router.navigate('/userHome/');
          }
        }
      },
      onSignupClicked(e){

      },
      onLogoutClicked() {
        
      },
      toUserReg(){
        this.$f7.views.main.router.navigate('/userReg/');
      }, 
      toAdminReg() { 
        this.$f7.views.main.router.navigate('/adminReg/');
      }
    },
    mounted() {
      navigator.geolocation.getCurrentPosition(
              position => {
              this.lat = position.coords.latitude;
              this.lng = position.coords.longitude;
            },
            error => {
              console.log(error.message);
            },
    )
    },
  };

</script>