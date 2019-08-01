<template>
  <div class="personal">
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
                  <a>地址管理</a>
                </li>
              </router-link>
              <router-link to="/like">
                <li>
                  <a style="color:#ff6700;font-weight:bold;">商品喜欢</a>
                </li>
              </router-link>
            </ul>
          </div>
        </div>
        <div class="rtcont fr"></div>
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
      userlist: [],
      dialogVisible: false,
      form: {}
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
          axios
            .get('/users/User_List/?search=' + this.username)
            .then(result => {
              console.log(result)
              this.userlist = result.data[0]
              console.log(this.userlist)
            })
            .catch(() => {})
        })
        .catch(() => {})
    },
    insertuser() {
      this.dialogVisible = true
      this.form = this.userlist
      delete this.form['password']
    },
    insertok(form) {
      this.dialogVisible = false
      axios
        .post('/users/User_Updated/', this.form)
        .then(result => {
          this.$notify.success({
            title: '成功',
            message: '修改个人信息成功'
          })
        })
        .catch(error => {
          this.findAll()
          this.$notify.error({
            title: '网络链接错误',
            message: '加载数据失败'
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
    }
  }
}
</script>
