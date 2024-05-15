<template>
  <div>
    <MainIndex v-if="currentComponent === 'MainIndex'" @login-success="handleLoginSuccess" />
    <LoginMenu v-else />
  </div>
</template>

<script>
import MainIndex from './components/MainIndex.vue'
import LoginMenu from './components/Login-menu.vue'

export default {
  name: 'App',
  components: {
    MainIndex,
    LoginMenu
  },
  data() {
    return {
      currentComponent: 'MainIndex'
    }
  },
  methods: {
    handleLoginSuccess() {
      this.currentComponent = 'LoginMenu'
    }
  }
}
</script>
