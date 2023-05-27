<template>
  <q-page class="">
    <div class="q-pa-md">
      <div class="row">
        <div v-for="(item, idx) in items" class="col-2" :key="idx">
          <q-img :src="item.image">
            <div class="absolute-bottom text-subtitle1 text-center">
              {{ item.item_name }} {{ item.item_price }}
              <q-btn color="primary" icon="check" @click="addToCart(item)" />
            </div>
          </q-img>
        </div>
      </div>

      <q-table
        title="Cart"
        :rows="currentCartData.items"
        :columns="cartColumns"
        :rows-per-page-options="[currentCartData.items.length]"
        :pagination="false"
        row-key="name"
      >
    
      <template v-slot:pagination>
        Total Cart: {{ currentCartData.price }}
        <q-btn
        color="primary"
        icon="check"
        label="Checkout"
        @click="checkoutCart()"
      />
      </template>
    </q-table>

   
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { api } from "boot/axios";
import Decimal from "decimal.js";

export default defineComponent({
  name: "IndexPage",
  data() {
    return {
      cartColumns: [
        {
          name: "name",
          align: "center",
          label: "Item",
          field: "name",
          sortable: true,
        },
        { name: "quantity", label: "Qty", field: "quantity", sortable: true },
        {
          name: "total_price",
          label: "Total Price",
          field: "total_price",
          format: val => new Decimal(val).toString(),
          sortable: true,
        },
      ],

      currentCartData: {
        items: [],
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
      console.log(this.currentCartData);
    },
    checkoutCart() {
      api.post("cart/checkout/", this.currentCartData).then((resp) => {
      });
    },
    getItems() {
      console.log("getItems");
      api.get("/items/").then((resp) => {
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
