<template>
  <div class="addorder ordersuccess" style="height:600px;">
    <div class="banner_x center">
      <div class="wdgwc fl ml40">支付订单</div>
      <div class="wxts fl ml20">温馨提示：产品是否购买成功，以最终下单为准哦，请尽快结算</div>
      <div class="clear"></div>
    </div>
    <div class="xiantiao"></div>
    <div style="width:80%;margin-left:10%;margin-top:30px;">
      <img src="../image/成功.png" alt style="width:100px;height:100px;float:left" />
      <span style="margin-left:100px;padding-left:100px;">
        <h1>&nbsp;&nbsp;&nbsp;&nbsp;订单提交成功！去付款咯~</h1>
      </span>
      <span style="float:right;margin-right:300px;;">
        <h3>应付总额：{{this.order.max_price}}&emsp;元</h3>
      </span>
      <br />
      <br />
      <br />
      <br />
      <br />
      <hr style="background-color:gainsboro;height:1px;border:none;width:80%;margin-left:10%" />
      <div style="margin-top:30px;font-size:20px;color:gray;margin-left:10%;">
        <ul>
          <li>
            订单号：
            <span>{{this.order.order_num}}</span>
          </li>
          <li>
            收货信息：
            <span>{{this.order.order_aceptman +'&emsp;'+ this.order.order_phone+'&emsp;'+this.order.order_address}}</span>
          </li>
          <li>
            商品名称：
            <span v-for="item in this.order.data" :key="item">{{item.good_name+'&emsp;'}}</span>
          </li>
          <li>
            配送方式：
            <span>包邮</span>
          </li>
        </ul>
        <br />
        <br />
        <hr style="background-color:gainsboro;height:1px;border:none;" />
      </div>
      <div style="margin-top:30px;float:right">
        <el-button @click="xuqiao">暂不支付</el-button>
        <el-button type="danger" @click="pay">立即支付</el-button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
export default {
  data() {
    return {
      user_id: '',
      username: '',
      order_id: '',
      order: []
    }
  },
  created() {
    this.findAll()
  },
  methods: {
    findAll() {
      this.order_id = this.$route.query.id
      axios
        .post('/wish/api-token-verify/', { token: Cookies.get('token') })
        .then(result => {
          this.user_id = result.data.user_id
          this.username = result.data.username
        })
        .catch(() => {})
      axios
        .get('/goods/Order_List/?order_num=' + this.order_id)
        .then(result => {
          console.log(result)
          this.order = result.data.result[0]
        })
        .catch(() => {})
    },
    xuqiao() {
      this.$router.push({ path: '/order' })
    },
    pay() {
      axios
        .post('/goods/ali_Pay/', {
          order_num: this.order.order_num,
          max_price: this.order.max_price
        })
        .then(result => {
          console.log(result.data.url)
          window.open(result.data.url)
        })
        .catch(error => {
          this.$notify.error({
            title: '跳转失败',
            message: '请检查网络哦'
          })
        })
    }
  }
}
</script>
<style scoped>
ul li span {
  color: #000;
}
ul li {
  margin-top: 20px;
}
</style>

