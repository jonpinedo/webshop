<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title> Qvantel Test Jon Pinedo </q-toolbar-title>

        <div>
          <q-btn
            v-show="loggedIn"
            color="primary"
            label="Logout"
            @click="logout"
          />
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import { getState } from "boot/state";

export default defineComponent({
  name: "MainLayout",
  setup() {
    const { loggedIn, setLoggedIn } = getState();
    const updateLoggedIn = (newValue) => {
      setLoggedIn(newValue);
    };
    return {
      loggedIn,
      updateLoggedIn,
    };
  },
  mounted() {
    console.log(this.loggedIn);
  },
  methods: {
    logout() {
      this.updateLoggedIn(false);
      localStorage.removeItem("token");
      this.$router.push("/login");
    },
  },
});
</script>
