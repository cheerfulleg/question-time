<template>
  <div id="app">
    <div id="nav">
      <Navbar :username="username"/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import {apiService} from "@/common/api.service";

export default {
  name: 'App',
  components: {Navbar},
data() {
    return {
      username: ''
    }
},
  methods: {
  async setUserInfo() {
    const data = await apiService("/api/user/");
    const requestUser = data['username'];
    window.localStorage.setItem('username', requestUser);
    this.username = requestUser;
  }
},
  created() {
    this.setUserInfo();
  }
}
</script>

<style>
html, body {
  height: 100%;
  font-family: "Playfair Display", serif;
}

.btn:focus {
  box-shadow: none !important;
}
</style>
