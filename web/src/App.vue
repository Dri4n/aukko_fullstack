<template>
  <div id="app">
     <transition name="page" mode="out-in">
        <div>
            <div class="row">
              <div class="col col-6 offset-md-3">
                <router-link to="/">
                  <img src="./assets/aukko_logo.jpg" class="image-responsive">
                </router-link>
              </div>
            </div>
            <br />
            <div class="container">
              <router-view/>
            </div>
        </div>
     </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}
</style>
