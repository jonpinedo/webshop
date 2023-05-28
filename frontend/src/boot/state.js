import { ref } from "vue";
const loggedIn = ref(false)

export function getState() {
    const setLoggedIn = (val) => {
        loggedIn.value = val
    }
    return {
        loggedIn, setLoggedIn
    }

}


