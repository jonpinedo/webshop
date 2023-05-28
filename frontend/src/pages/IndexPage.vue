<template>
  <q-page class="">
    <div class="q-pa-md">
      <div class="q-col-gutter-md row items-start">
        <div v-for="(item, idx) in items" class="col-lg-2 col-sm-6 col-xs-12" :key="idx">
          <q-img heigh="500" :src="item.image">
            <div class="absolute-bottom text-subtitle1 text-center">
              {{ item.item_name }} <strong>{{ item.item_price }}$</strong>
              <q-btn size="xs" color="primary" icon="add" @click="addToCart(item)" />
            </div>
          </q-img>
        </div>
      </div>
      <q-dialog v-model="dialog" persistent>
        <q-card>
          <q-toolbar>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo.svg" />
            </q-avatar>

            <q-toolbar-title
              ><span class="text-weight-bold"
                >Order {{ order_confirmation.id }} details</span
              >
            </q-toolbar-title>
          </q-toolbar>
          <q-card-section class="row items-center">
            <q-table
              flat
              separator="vertical"
              :rows="order_confirmation.items"
              :columns="cartColumns"
              :rows-per-page-options="[order_confirmation.items.length]"
              :pagination="false"
              row-key="name"
            >
              <template v-slot:pagination>
                Total Cart: {{ order_confirmation.price }}
              </template>
            </q-table>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="OK" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <div class="q-pa-md">
        <q-table
          v-show="currentCartData.items.length > 0"
          separator="vertical"
          title="Cart"
          :rows="currentCartData.items"
          :columns="cartColumns"
          :rows-per-page-options="[currentCartData.items.length]"
          :pagination="false"
          row-key="name"
        >
          <template v-slot:pagination>
            <div class="float-right">
              Total Cart: {{ currentCartData.price }}
            </div>
          </template>
        </q-table>
      </div>
      <div class="q-pa-md">
        <q-btn
          v-if="currentCartData.items.length > 0"
          color="primary"
          icon="check"
          label="Checkout"
          @click="checkoutCart()"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { api } from "boot/axios";
import Decimal from "decimal.js";
import { Notify } from 'quasar'

export default defineComponent({
  name: "IndexPage",
  data() {
    return {
      dialog: false,
      order_confirmation: [],
      cartColumns: [
        {
          name: "name",
          align: "left",
          label: "Item",
          field: "name",
          sortable: true,
        },
        { name: "quantity", label: "Qty", field: "quantity", sortable: true },
        {
          name: "total_price",
          label: "Total Price",
          field: "total_price",
          format: (val) => new Decimal(val).toString(),
          sortable: true,
        },
      ],

      currentCartData: {
        items: ref([]),
        country_code: "en",
        price: new Decimal(0),
      },
      items: [],
    };
  },

  methods: {
    addToCart(new_item) {
      console.log("addToCart");
      var item_found = false;
      var current_item = {
        item: new_item.item_id,
        name: new_item.item_name,
        price: new Decimal(new_item.item_price).toString(),
        quantity: 1,
        total_price: new Decimal(new_item.item_price).toString(),
      };
      var i = 0;
      for (const item of this.currentCartData.items) {
        if (current_item.item == item.item) {
          item_found = true;
          this.currentCartData.items[i].quantity += 1;
          this.currentCartData.items[i].total_price = new Decimal(
            this.currentCartData.items[i].quantity *
              this.currentCartData.items[i].price
          ).toString();
          this.currentCartData.price = new Decimal(this.currentCartData.price)
            .plus(this.currentCartData.items[i].price)
            .toString();
          break;
        }
        i++;
      }
      if (!item_found) {
        this.currentCartData.items.push(current_item);
        this.currentCartData.price = new Decimal(this.currentCartData.price)
          .plus(current_item.price)
          .toString();
      }
      Notify.create({
  message: new_item.item_name + " added to cart"
})
      console.log(this.currentCartData);
    },
    checkoutCart() {
      api.post("/api/cart/checkout/", this.currentCartData).then((resp) => {
        Notify.create({message: "Order processed successfully", color: "purple"})
        api.get("/api/cart/" + resp.data.cart_id + "/").then((resp2) => {
          this.currentCartData.items = [];
          this.currentCartData.price = new Decimal(0);
          this.order_confirmation = resp2.data;
          this.dialog = true;
        });
      });
    },
    getItems() {
      console.log("getItems");
      api.get("/api/items/").then((resp) => {
        this.items = resp.data;
      });
    },
  },

  mounted() {
    console.log("mounted");
    this.getItems();
  },
});
</script>
