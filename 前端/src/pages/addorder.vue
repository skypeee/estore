<template>
  <div class="addorder shopping">
    <!-- 确认订单 -->
    <div class="banner_x center">
      <div class="wdgwc fl ml40">确认订单</div>
      <div class="wxts fl ml20">温馨提示：产品是否购买成功，以最终下单为准哦，请尽快结算</div>
      <div class="clear"></div>
    </div>
    <div class="xiantiao"></div>
    <div style="width:80%;margin-left:10%;">
      <!-- 收获地址 -->
      <h3 style="margin-left:50px;margin-top:30px;margin-bottom:30px;">收货地址</h3>
      <el-radio-group v-model="radio">
        <div
          class="caozuo"
          style="width:230px;height:160px;border:solid 1px #e4e7ed;margin-left:40px;margin-bottom:30px;float:left;line-height:25px;padding-left:20px;padding-top:20px"
          v-for="item in res_list"
          :key="item"
        >
          <el-radio :label="item.id">
            <p style="font-size:23px;margin-bottom:30px;margin-top:10px;">{{item.name}}</p>
            <p style="color:grey;margin-bottom:10px;">{{item.phone}}</p>
            <div
              style="color:grey;margin-bottom:10px;width:200px;height: auto;overflow: hidden;"
            >{{item.content}}</div>
          </el-radio>
        </div>
      </el-radio-group>
      <div
        style="width:230px;height:160px;border:solid 1px #e4e7ed;margin-left:40px;line-height:160px; float:left;margin-bottom:30px;padding-left:20px;padding-top:20px"
      >
        <el-button
          type="primary"
          icon="el-icon-plus"
          circle
          style="margin-left:80px;"
          @click="dialog"
        ></el-button>
      </div>
      <div class="page" style="float:left;margin-left:80%">
        <el-pagination
          background
          prev-text="上一页"
          @current-change="handleCurrentChange2"
          next-text="下一页"
          layout="prev, pager, next"
          :total="total"
          :page-size="3"
          style="margin-top: 5px;float: right;margin-right: 15px;"
        ></el-pagination>
      </div>
      <div class="clear"></div>
      <br />
      <hr style="background-color:gainsboro;height:1px;border:none;" />
      <!-- 商品 -->
      <div>
        <h3 style="margin-left:50px;margin-top:30px;margin-bottom:30px;">商品</h3>
        <el-table
          ref="multipleTable"
          :data="tableData"
          tooltip-effect="dark"
          style="width: 90%;margin-left:50px;"
        >
          <el-table-column prop="good.good_img" label="商品图片">
            <template slot-scope="scope">
              <img :src="scope.row.good.good_img" alt width="70px;" height="80px;" />
            </template>
          </el-table-column>
          <el-table-column prop="good.good_name" label="商品名称"></el-table-column>
          <el-table-column prop="good.good_price" label="单价"></el-table-column>
          <el-table-column prop="good_num" label="数量" show-overflow-tooltip>
            <template slot-scope="scope">{{scope.row.good_num}}</template>
          </el-table-column>
          <el-table-column label="小计" show-overflow-tooltip>
            <template slot-scope="scope">{{scope.row.good_num * scope.row.good.good_price}}</template>
          </el-table-column>
        </el-table>
        <br />
        <hr style="background-color:gainsboro;height:1px;border:none;" />
      </div>
      <!-- 配送方式 -->
      <div>
        <h3 style="margin-left:50px;margin-top:30px;margin-bottom:30px;">
          配送方式
          <span style="color:orange;margin-left:50px;font-weight:500">包邮</span>
        </h3>
        <br />
        <hr style="background-color:gainsboro;height:1px;border:none;" />
      </div>
      <br />
      <br />
      <!-- 订单信息 -->
      <div style="margin-left:80%;color:gray">
        <ul class="Ul">
          <li>
            商品件数：
            <span>{{this.count}} 件</span>
          </li>
          <li>
            商品总价：
            <span>{{this.pricenum}} 元</span>
          </li>
          <li>
            活动优惠：
            <span>0 元</span>
          </li>
          <li>
            优惠卷抵扣：
            <span>0 元</span>
          </li>
          <li>
            运费：
            <span>0 元</span>
          </li>
          <br />
          <li>
            应付总额：
            <span>{{this.pricenum}} 元</span>
          </li>
        </ul>
      </div>
      <br />
      <hr style="background-color:gainsboro;height:1px;border:none;" />
      <br />
      <br />
      <div style="margin-left:80%;">
        <el-button @click="shopping">返回购物车</el-button>
        <el-button type="danger" @click="jiesuan">去结算</el-button>
      </div>
      <br />
      <br />
    </div>
    <el-dialog
      title="添加收货人信息"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="收件人" prop="name" label-text-align="center">
          <el-input v-model="form.name" size="mini"></el-input>
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="form.phone" size="mini"></el-input>
        </el-form-item>
        <el-form-item label="收货地址">
          <el-input v-model="form.content" size="mini"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="confirm(form)">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
export default {
  data() {
    return {
      username: '', //用户id
      dialogVisible: false, //模态框
      form: {}, //新增收获信息form
      total: 6, //分页总条数
      page: 1, //当前页数
      res_list: [], //地址列表
      radio: 0, //单选
      tableData: [], //商品列表
      favoriteid: [], //购物车id列表
      count: 0, //商品件数
      pricenum: 0, //订单总价
      favorite_id: [], //购物车id列表
      form3: {} //创建订单
    }
  },
  created() {
    this.findAll()
  },
  methods: {
    //   加载数据
    findAll() {
      axios
        .post('/wish/api-token-verify/', { token: Cookies.get('token') })
        .then(result => {
          this.username = result.data.user_id
          this.username_name = result.data.username
        })
        .catch(() => {})
      axios
        .get(
          '/users/Address_List/?page=' +
            this.page +
            '&page_size=+3+&search=' +
            this.username
        )
        .then(result => {
          console.log(result)
          this.res_list = result.data.results
          this.total = result.data.count
          this.radio = result.data.results[0].id
        })
      this.favoriteid = this.$route.query.id
      this.pricenum = this.$route.query.pricenum
      console.log(this.favoriteid)
      this.tableData = []
      this.favorite_id = []
      this.count = 0
      this.favoriteid.forEach(item => {
        console.log(item)
        this.favorite_id.push(item)
        axios
          .get('/goods/Favorite_List/?search=' + this.username + '&id=' + item)
          .then(result => {
            console.log(result.data.results)
            this.tableData.push(result.data.results[0])
            this.count += 1
          })
      })
    },
    // 显示模态框
    dialog() {
      this.dialogVisible = true
    },
    // 新增收获信息
    confirm() {
      axios
        .post('/users/Address_Created/', {
          content: this.form.content,
          name: this.form.name,
          phone: this.form.phone,
          user: this.username
        })
        .then(result => {
          this.dialogVisible = false
          this.findAll()
          this.$notify.success({
            title: '添加收货信息成功',
            message: '添加收货信息成功'
          })
        })
    },
    // 关闭模态框
    handleClose() {
      this.dialogVisible = false
      if (this.$refs['form'] != undefined) {
        this.$refs['form'].resetFields()
      }
      this.form = {}
      this.findAll()
    },
    // 分页
    handleCurrentChange2(val) {
      this.page = val
      console.log(this.page)
      this.findAll()
    },
    // 购物车
    shopping() {
      this.$router.push({ path: '/shopping' })
    },
    // 创建订单
    jiesuan() {
      if (this.radio == 0) {
        this.$notify.error({
          title: '请选择收获地址',
          message: '请选择收获地址'
        })
      } else {
        this.form3['order_address'] = this.radio
        // var timestamp = Date.parse(new Date())
        // console.log(timestamp)
        this.form3['order_num'] = this.datatime() + this.username
        this.form3['id'] = this.favorite_id
        this.form3['user_name'] = this.username_name
        console.log(this.form3)
        axios
          .post('/goods/Border_Created/', this.form3)
          .then(result => {
            this.$router.push({
              path: '/ordersuccess',
              query: { id: this.form3.order_num }
            })
            this.$notify.success({
              title: '订单创建成功',
              message: '订单创建成功'
            })
          })
          .catch(error => {
            this.$notify.error({
              title: '订单创建失败',
              message: '订单创建失败'
            })
          })
      }
    },
    datatime() {
      var date = new Date()
      var year = date.getFullYear()
      var month = date.getMonth() + 1
      var strDate = date.getDate()
      if (month >= 1 && month <= 9) {
        month = '0' + month
      }
      if (strDate >= 0 && strDate <= 9) {
        strDate = '0' + strDate
      }
      var hour = date.getHours()
      var minute = date.getMinutes()
      var s = date.getSeconds()
      var currentdate = year + month + strDate + hour + minute + s
      console.log(currentdate)
      return currentdate
    }
  }
}
</script>
<style scoped>
.caozuo a {
  color: orange;

  font-weight: 500;
}
.caozuo a:hover {
  color: orangered;
  font-weight: 1000;
}
li span {
  color: orangered;
}
</style>

