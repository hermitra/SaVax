<template>
  <f7-page name="home">
  <!-- Top Navbar -->
    <f7-navbar :sliding="false" large>
      <div>
        <f7-button class = "button-fill button" v-on:click="goBack()" style="text-align:left; width:100%"> Go Back </f7-button>
      </div>
      <h4 style="text-align:right; width: 100%;color: #005eb8;"> <div class="shadow_corner"><img class="logo" src="static/icons/logo.png" /></div></h4>
      <f7-nav-title-large sliding style="text-align:center; width: 100%; color: #005eb8"> Admin Registration </f7-nav-title-large>
    </f7-navbar>

  <!-- Page content-->

  <f7-block strong>
    <form @submit.prevent="onSignupClicked" action="" method="GET">
      <f7-list class = "login-list" no-hairlines-md>
        <f7-list-input class="email-input" :value="name" @input="name = $event.target.value" label="Enter your name" placeholder="John Smith" />
        <f7-list-input class="email-input" :value="email" @input="email = $event.target.value" label="Type in your work email address" type="email" placeholder="E-mail" />
        <f7-list-input :value="password" @input="password = $event.target.value" label="Choose a password" type ="password" placeholder="Password" />
        <f7-list-input :value="clinic" @input="clinic = $event.target.value" label="What is your clinic" type ="clinic" placeholder="Clinic" />
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
        clinic:'',
        password: '',
        loggedOn: false, // can set to true when testing
      };
    },
    methods: {
      goBack() {
        this.$f7.views.main.router.navigate('/login/');
      },
      onSignupClicked(e){
        var res = {
          "name":this.name,
          "work.email": this.email,
          "clinicName": this.clinic,
          "password": this.password
        }
        axios.post('/adminReg/', res).then((response)=>{
              this.loggedOn = response.data.response;
        }) 
        if(this.loggedOn){
          console.log(res);
          this.$root.email = this.email;
          this.$f7.views.main.router.navigate('/adminHome/');
        }
      },
      
    },
      
  };

</script>