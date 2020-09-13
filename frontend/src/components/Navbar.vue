<template>
  <nav class="navbar navbar-expand navbar-light bg-light my-navbar">
    <div class="container">
      <router-link
          :to="{name: 'home'}"
          class="navbar-brand qt-navbar"
      >
        Question Time
      </router-link>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
            <p class="btn btn-sm btn-disabled m-1"><strong>{{ username }}</strong> </p>
          </li>
          <li class="nav-item">
            <router-link
                :to="{name: 'question-editor'}"
                class="btn btn-sm btn-danger m-1"
            >
              Ask Question
            </router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary m-1" href="/accounts/logout/">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  props: {
    username: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #DDD;
}

.qt-navbar {
  font-weight: bold;
  font-size: 130%;
}

.qt-navbar:hover {
  color: darkred !important;
}
</style>