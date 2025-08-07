<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/monitoring_and_automation.png" width="125" height="125" />
    <div class="wrapper">
      <HelloWorld msg="Monitoring and Automation" />
    </div>
  </header>

  <main>
    <ButtonPanel />
  </main>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import ButtonPanel from './components/ButtonPanel.vue';

export default {
    components: { HelloWorld, ButtonPanel },
    data() {
      return {
      };
    },
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
    margin-top: 30px; /* Adjust the value as needed */
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
