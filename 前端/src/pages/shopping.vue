<template>
  <div class="shopping">
    <!-- 购物车页面 -->
    <div class="banner_x center">
      <div class="wdgwc fl ml40">我的购物车</div>
      <div class="wxts fl ml20">温馨提示：产品是否购买成功，以最终下单为准哦，请尽快结算</div>
      <div class="clear"></div>
    </div>
    <div class="xiantiao"></div>
    <el-table
      ref="multipleTable"
      :data="tableData"
      tooltip-effect="dark"
      style="width: 80%;margin-left:150px;"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="good.good_img" label="商品图片" width="120">
        <template slot-scope="scope">
          <img :src="scope.row.good.good_img" alt width="70px;" height="80px;" />
        </template>
      </el-table-column>
      <el-table-column prop="good.good_name" label="商品名称" width="120"></el-table-column>
      <el-table-column prop="good.good_price" label="单价" width="120"></el-table-column>
      <el-table-column prop="good_num" label="数量" show-overflow-tooltip>
        <template slot-scope="scope">
          <el-input-number
            size="mini"
            v-model="scope.row.good_num"
            @change="handleChange(scope.row)"
            :min="1"
            :max="10"
            label="描述文字"
          ></el-input-number>
        </template>
      </el-table-column>
      <el-table-column label="小计" show-overflow-tooltip>
        <template slot-scope="scope">{{scope.row.good_num * scope.row.good.good_price}}</template>
      </el-table-column>
      <el-table-column label="操作" show-overflow-tooltip>
        <template slot-scope="scope">
          <el-button type="danger" icon="el-icon-delete" circle @click="Delete(scope.row)"></el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="gwcxqbj">
      <div class="jiesuandan mt20 center">
        <div class="tishi fl ml20">
          <ul>
            <li>
              <router-link to="/contentList?id= ">继续购物</router-link>
            </li>
            <li>|</li>
            <li>
              共
              <span></span>
              {{this.count}}件商品，已选择
              <span>{{this.total}}</span>件
            </li>
            <div class="clear"></div>
          </ul>
        </div>

        <div class="jiesuan fr">
          <div class="jiesuanjiage fl">
            合计（不含运费）：
            <span>{{this.pricenum}}元</span>
          </div>
          <div class="jsanniu fr">
            <input class="jsan" @click="yanzheng" name="jiesuan" value="             去结算" />
          </div>
          <div class="clear"></div>
        </div>
        <div class="clear"></div>
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
      username: '',
      pricenum: 0,
      tableData: [],
      form: { order_aceptman: '', order_phone: '', order_address: '' },
      multipleSelection: [],
      count: 0,
      total: 0,
      dingdan: [],
      userlist: []
      // dialogVisible:false,
    }
  },
  created() {
    this.findAll()
    axios
      .post('/wish/api-token-verify/', { token: Cookies.get('token') })
      .then(result => {
        console.log(result)
        this.username = result.data.user_id
        console.log('ok')
      })
      .catch(() => {
        console.log(this.token)
      })
  },
  methods: {
    findAll() {
      axios
        .get('/goods/Favorite_List/?search=' + this.username)
        .then(result => {
          console.log(result.data.count)
          this.tableData = result.data.results
          this.count = result.data.count
        })
      axios.get('/users/User_List/?search=' + this.username).then(result => {
        console.log(result)
        this.userlist = result.data[0]
      })
    },
    handleSelectionChange(val) {
      this.multipleSelection = val
      console.log(this.multipleSelection)
      this.pricenum = 0
      this.total = this.multipleSelection.length
      this.dingdan = []
      this.multipleSelection.forEach(item => {
        console.log(item)
        this.dingdan.push(item.id)
        this.pricenum += item.good_num * item.good.good_price
      })
    },
    Delete(row) {
      console.log(row.id)
      axios
        .post('/goods/Favorite_Delete/', { id: row.id })
        .then(result => {
          this.findAll()
          this.multipleSelection = []
          this.$notify.success({
            title: '移出购物车商品成功',
            message: '移出购物车商品成功'
          })
        })
        .catch(error => {
          this.$notify.error({
            title: '移出购物车商品失败',
            message: '移出购物车商品失败'
          })
        })
    },

    //   商品数量
    // 验证收货信息
    yanzheng() {
      this.$router.push({
        path: '/addorder',
        query: { id: this.dingdan, pricenum: this.pricenum }
      })
    },
    handleChange(row) {
      axios
        .post('/goods/Favorite_Update/', { id: row.id, good_num: row.good_num })
        .then(result => {
          console.log(result)
          this.findAll()
          this.$notify.success({
            title: '修改成功',
            message: '修改数量成功'
          })
        })
    }
  }
}
</script>