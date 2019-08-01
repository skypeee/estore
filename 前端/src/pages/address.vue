<template>
  <div class="address">
    <!-- 个人详情页 -->
    <!-- self_info -->
    <div class="grzxbj">
      <div class="selfinfo center">
        <div class="lfnav fl">
          <div class="ddzx">订单中心</div>
          <div class="subddzx">
            <ul>
              <router-link to="order">
                <li>
                  <a>我的订单</a>
                </li>
              </router-link>
            </ul>
          </div>
          <div class="ddzx">个人中心</div>
          <div class="subddzx">
            <ul>
              <router-link to="/personal">
                <li>
                  <a>我的个人中心</a>
                </li>
              </router-link>
              <router-link to="/address">
                <li>
                  <a style="color:#ff6700;font-weight:bold;">地址管理</a>
                </li>
              </router-link>
              <router-link to="/like">
                <li>
                  <a>商品喜欢</a>
                </li>
              </router-link>
            </ul>
          </div>
        </div>
        <div class="rtcont fr">
          <div class="grzlbt ml40">收货地址</div>
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
          <div
            class="caozuo"
            style="width:230px;height:160px;border:solid 1px #e4e7ed;margin-left:40px;margin-bottom:30px;float:left;line-height:25px;padding-left:20px;padding-top:20px"
            v-for="item in res_list"
            :key="item"
          >
            <p style="font-size:23px;margin-bottom:15px;">{{item.name}}</p>
            <p style="color:grey">{{item.phone}}</p>
            <p style="color:grey;margin-bottom:10px;">{{item.content}}</p>
            <a style="float:right;margin-right:5px;cursor: pointer;" @click="shanchu(item.id)">删除</a>
            <a style="float:right;margin-right:5px;cursor: pointer;" @click="xiugai(item)">修改</a>
          </div>
        </div>
        <div class="page">
          <el-pagination
            background
            prev-text="上一页"
            @current-change="handleCurrentChange2"
            next-text="下一页"
            layout="prev, pager, next"
            :total="total"
            :page-size="5"
            style="margin-top: 5px;float: right;margin-right: 15px;"
          ></el-pagination>
        </div>
        <div class="clear"></div>
      </div>
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
    <el-dialog
      title="修改收货人信息"
      :visible.sync="dialogVisible2"
      width="30%"
      :before-close="handleClose2"
    >
      <el-form ref="form2" :model="form2" label-width="80px">
        <el-form-item label="收件人" prop="name" label-text-align="center">
          <el-input v-model="form2.name" size="mini" :placeholder="this.formdatd.name"></el-input>
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="form2.phone" size="mini" :placeholder="this.formdatd.phone"></el-input>
        </el-form-item>

        <el-form-item label="收货地址">
          <el-input v-model="form2.content" size="mini" :placeholder="this.formdatd.content"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible2 = false">取 消</el-button>
        <el-button type="primary" @click="queding(form)">确 定</el-button>
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
      username: '',
      userlist: [],
      dialogVisible: false,
      form: {},
      total: 6,
      page: 1,
      res_list: [],
      form2: {},
      formdatd: { name: '', phone: '', content: '' },
      dialogVisible2: false
    }
  },
  created() {
    this.findAll()
  },

  methods: {
    findAll() {
      axios
        .post('/wish/api-token-verify/', { token: Cookies.get('token') })
        .then(result => {
          this.username = result.data.user_id
        })
        .catch(() => {})
      axios
        .get(
          '/users/Address_List/?page=' +
            this.page +
            '&page_size=+5+&search=' +
            this.username
        )
        .then(result => {
          console.log(result)
          this.res_list = result.data.results
          this.total = result.data.count
        })
    },
    dialog() {
      this.dialogVisible = true
    },
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
    handleClose() {
      this.dialogVisible = false
      if (this.$refs['form'] != undefined) {
        this.$refs['form'].resetFields()
      }
      this.form = {}
      this.findAll()
    },
    handleCurrentChange2(val) {
      this.page = val
      console.log(this.page)
      this.findAll()
    },
    shanchu(id) {
      axios
        .post('/users/Address_Deleted/', { id: id })
        .then(result => {
          this.findAll()
          this.$notify.success({
            title: '删除成功',
            message: '删除成功'
          })
        })
        .catch(error => {
          this.$notify.error({
            title: '删除失败',
            message: '删除失败'
          })
        })
    },
    xiugai(order) {
      this.form2 = { name: '', phone: '', content: '' }
      this.formdatd = order
      console.log(order)
      this.dialogVisible2 = true
    },
    handleClose2() {
      this.dialogVisible2 = false
      if (this.$refs['form2'] != undefined) {
        this.$refs['form2'].resetFields()
      }
    },
    queding(form) {
      this.form2['id'] = this.formdatd.id
      this.form2['user'] = this.formdatd.user
      if (this.form2['name'] == '') {
        this.form2['name'] = this.formdatd.name
      }
      if (this.form2['phone'] == '') {
        this.form2['phone'] = this.formdatd.phone
      }
      if (this.form2['content'] == '') {
        this.form2['content'] = this.formdatd.content
      }
      console.log(this.form2)
      axios
        .post('/users/Address_Update/', this.form2)
        .then(result => {
          this.findAll()
          this.dialogVisible2 = false

          this.$notify.success({
            title: '修改收货人信息成功',
            message: '修改收货人信息成功'
          })
        })
        .catch(error => {
          this.dialogVisible2 = false
          this.$notify.error({
            title: '修改收货人信息失败',
            message: '修改收货人信息失败'
          })
        })
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
</style>

