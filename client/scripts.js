import HttpRequest from "./etc/js/http.js";

(function () {
    "use strict";

    let http = new HttpRequest();

    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue!",
            smartHubElements: [
                {
                    key: 1,
                    name: "Ngrok",
                    endpoints: {
                        status: "/status/ngrok",
                    },
                    running: false,
                    loading: true,
                },
                {
                    key: 2,
                    name: "Samsung REST",
                    endpoints: {
                        status: "/status/samsung",
                    },
                    running: false,
                    loading: true,
                },
            ],
        },
        methods: {
            updatePayloadObject(referenceObject, updatedValue) {
                console.log("referenceObject");
                console.log(referenceObject);
                console.log("updatedValue");
                console.log(updatedValue);
                this.$set(
                    this.smartHubElements,
                    referenceObject.running,
                    updatedValue
                );
            },
            getElementStatus() {
                this.smartHubElements.forEach((el) => {
                    http.get(el.endpoints.status)
                        .then((response) => {
                            console.log(response);
                            el.running = response.status;
                        })
                        .catch((error) => {
                            console.log(error);
                            el.running = false;
                        }).then(() => {
                            el.loading = false;
                        });
                });
            },
            toggle(elementKey) {
                console.log(`clicou no ${elementKey}`);
                this.smartHubElements.forEach((el) => {
                    if (el.key == elementKey) {
                        if (!el.running) {
                            // ver qual clicou
                            // startar
                            // ligar o loading
                            // esperar iniciar
                            el.running = true;
                        } else {
                            console.log("Already running");
                        }
                    }
                });
            },
        },
        async mounted() {
            this.getElementStatus();
        },
    });
})();
