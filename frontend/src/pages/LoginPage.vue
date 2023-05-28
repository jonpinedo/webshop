<template>
  <q-page
    class="row justify-center items-center"
    style="background: linear-gradient(#8274c5, #5a4a9f)"
  >
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width: 400px; height: 540px">
          <q-card-section class="bg-deep-purple-7">
            <h4 class="text-h5 text-white q-my-md">{{ title }}</h4>
          </q-card-section>
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl">
              <q-input
                ref="username"
                square
                clearable
                v-model="username"
                type="text"
                lazy-rules
                :rules="[this.required, this.short]"
                label="Username"
              >
                <template v-slot:prepend>
                  <q-icon name="person" />
                </template>
              </q-input>
              <q-input
                ref="password"
                square
                clearable
                v-model="password"
                :type="passwordFieldType"
                lazy-rules
                :rules="[this.required, this.short]"
                label="Password"
              >
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
                <template v-slot:append>
                  <q-icon
                    :name="visibilityIcon"
                    @click="switchVisibility"
                    class="cursor-pointer"
                  />
                </template>
              </q-input>
            </q-form>
          </q-card-section>

          <q-card-actions class="q-px-lg">
            <q-btn
              unelevated
              size="lg"
              color="secondary"
              @click="submit"
              class="full-width text-white"
              :label="btnLabel"
            />
          </q-card-actions>
          <q-card-section v-if="!register" class="text-center q-pa-sm">
            <p class="text-grey-6">Forgot password?</p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>
<script>
import { defineComponent, ref } from "vue";
import { api } from "boot/axios";
import { getState } from "boot/state";

export default defineComponent({
  setup() {
    const { setLoggedIn } = getState();
    const updateLoggedIn = (newValue) => {
      setLoggedIn(newValue);
    };
    return {
      updateLoggedIn,
    };
  },
  data() {
    return {
      title: "Login",
      username: "",
      password: "",
      repassword: "",
      passwordFieldType: "password",
      btnLabel: "Submit",
      visibility: false,
      visibilityIcon: "visibility",
    };
  },

  methods: {
    required(val) {
      return (val && val.length > 0) || "Field required";
    },
    diffPassword(val) {
      const val2 = this.$refs.password.value;
      return (val && val === val2) || "Both passwords do not match";
    },
    short(val) {
      return (val && val.length > 3) || "Password too short";
    },
    isEmail(val) {
      const emailPattern =
        /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
      return emailPattern.test(val) || "Invalid email";
    },
    submit() {
      this.$refs.username.validate();
      this.$refs.password.validate();
      const data = {
        username: this.username,
        password: this.password,
      };
      api.post("/login/", data).then((resp) => {
        const token = resp.data.access;
        localStorage.setItem("token", token);
        //Redirect to Index
        this.updateLoggedIn(true);
        this.$router.push("/");
      });
    },
    switchTypeForm() {
      this.register = !this.register;
      this.title = this.register ? "New user" : "Login";
      this.btnLabel = this.register ? "Sign in" : "Submit";
    },
    switchVisibility() {
      this.visibility = !this.visibility;
      this.passwordFieldType = this.visibility ? "text" : "password";
      this.visibilityIcon = this.visibility ? "visibility_off" : "visibility";
    },
  },
});
</script>
