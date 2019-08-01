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
                  <a style="color:#ff6700;font-weight:bold;">我的个人中心</a>
                </li>
              </router-link>
              <router-link to="/address">
                <li>
                  <a>地址管理</a>
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
          <div class="grzlbt ml40">
            我的资料
            <el-button
              style="margin-left:20px;"
              type="warning"
              icon="el-icon-edit"
              circle
              @click="insertuser"
            ></el-button>
            <i
              class="el-icon-warning"
              style="margin-left:10px;"
              size="mini"
              title="修改密码"
              @click="pass"
            ></i>
          </div>
          <div
            style="height：100px;margin-left:40px;line-height:100px;width:900px;border:1px solid #aaa;margin-top:10px;border-radius:3px;"
          >
            <span
              style="font-size:15px;font-weight:bold;color:rgb(117,117,117);padding-left:20px;"
            >头像</span>
            <span style="padding-left:130px;">
              <img
                :src="this.userlist.user_img?this.userlist.user_img:'../static/index/images/icon1.png'"
                alt
                style="width:80px;height:80px;border-radius: 100%;border: 1px solid #fff;margin-top:40px;display:inline-block"
              />
            </span>
          </div>

          <div class="subgrzl ml40">
            <span>昵称</span>
            <span>{{this.userlist.last_name}}</span>
          </div>
          <div class="subgrzl ml40">
            <span>手机号</span>
            <span>{{this.userlist.user_phone}}</span>
          </div>
          <div class="subgrzl ml40">
            <span>个性签名</span>
            <span>{{this.userlist.user_signature}}</span>
          </div>
          <div class="subgrzl ml40">
            <span>收货地址</span>
            <span>{{this.userlist.user_address}}</span>
          </div>

          <el-dialog
            title="修改个人信息"
            :visible.sync="dialogVisible"
            width="50%"
            :before-close="handleClose"
          >
            <el-form ref="form" :model="form" label-width="80px">
              <el-form-item label="用户头像" prop="user_img" label-text-align="center">
                <el-upload
                  style="margin-right:50%;"
                  class="avatar-uploader"
                  action="123"
                  :show-file-list="false"
                  :on-success="handleAvatarSuccess"
                  :on-change="onchange"
                  :before-upload="beforeAvatarUpload"
                >
                  <img
                    v-if="imageUrl"
                    :src="imageUrl"
                    class="avatar"
                    style="width:100px;height:100px;border-radius: 100%;border: 2px solid #fff;"
                  />
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </el-form-item>
              <el-form-item label="昵称" prop="last_name" label-text-align="center">
                <el-input v-model="form.last_name" size="mini" placeholder="请输入用户名"></el-input>
              </el-form-item>
              <el-form-item label="手机号">
                <el-input v-model="form.user_phone"></el-input>
              </el-form-item>
              <el-form-item label="个性签名">
                <el-input v-model="form.user_signature"></el-input>
              </el-form-item>
              <el-form-item label="收货地址">
                <el-input v-model="form.user_address"></el-input>
              </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
              <el-button @click="dialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="insertok">确 定</el-button>
            </span>
          </el-dialog>
        </div>
        <div class="Dialog">
          <el-dialog
            title="修改用户密码"
            :visible.sync="dialogFormVisible5"
            :before-close="closeForm5Dialog"
            top="100px"
          >
            <el-form :model="form5" ref="form5" class="demo-ruleForm">
              <el-form-item
                label="用户密码"
                prop="password"
                :label-width="formLabelWidth"
                label-text-align="center"
              >
                <el-input v-model="form5.password" size="mini" type="password" placeholder="请输入密码"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button size="small" type="primary" @click="Passinsert('form')">确 定</el-button>
            </div>
          </el-dialog>
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
      userlist: [],
      dialogVisible: false,
      imageUrl: '../../static/index/images/icon1.png',
      form: {},
      dialogFormVisible5: false,
      form5: {},
      formLabelWidth: '500px;'
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
      this.blobb = ''
      this.imageUrl = this.userlist.user_img
      delete this.form['password']
    },
    insertok(form) {
      this.dialogVisible = false
      var formData = new FormData()
      formData.append('user_address', this.form.user_address)
      formData.append('last_name', this.form.last_name)
      formData.append('user_signature', this.form.user_signature)
      formData.append('id', this.form.id)
      formData.append('user_phone', this.form.user_phone)
      if (this.blobb != '') {
        formData.append('user_img', this.blobb, 'userimg.jpg')
      }
      formData.forEach(item => {
        console.log(item)
      })
      var options = {
        url: '/users/User_Updated/',
        data: formData,
        method: 'post',
        contentType: false,
        headers: { 'Content-Type': 'multipart/form-data' }
      }
      axios(options)
        .then(result => {
          this.dialogFormVisible = false
          this.$notify.success({
            title: '成功',
            message: '修改用户信息成功'
          })
          this.findAll()
        })
        .catch(() => {
          this.$notify.error({
            title: '网络链接错误',
            message: '修改用户信息失败'
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
    pass() {
      this.dialogFormVisible5 = true
    },
    closeForm5Dialog() {
      this.dialogFormVisible5 = false
      if (this.$refs['form'] != undefined) {
        this.$refs['form'].resetFields()
      }
      this.form5 = {}
      this.findAll()
    },
    Passinsert(form) {
      if (this.form5.password) {
        axios
          .post('/users/User_Updated/', {
            id: this.username,
            password: this.form5.password
          })
          .then(result => {
            console.log(result)
            this.dialogFormVisible = false
            this.$notify.success({
              title: '修改用户密码成功',
              message: '修改用户密码成功，请重新登陆'
            })
            this.$root.currentComponent = 'login'
          })
          .catch(() => {
            this.$notify.error({
              title: '网络链接错误',
              message: '修改用户信息密码'
            })
          })
      } else {
        this.$notify.error({
          title: '密码不能为空',
          message: '密码不能为空'
        })
      }
    },
    handleAvatarSuccess(res, file) {
      // 上传用户头像成功的函数
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload(file) {
      // 上传图片的条件
      // const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2
      // if (!isJPG) {
      //   this.$message.error("上传头像图片只能是 JPG 格式!");
      // }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    onchange(file, fileList) {
      //当上传图片后，调用onchange方法，获取图片本地路径
      console.log('file:', file)

      var _this = this
      var event = event || window.event
      var file = event.target.files[0]
      var reader = new FileReader()
      //转base64
      reader.onload = function(e) {
        _this.imageUrl = e.target.result //将图片路径赋值给src
        _this.img = e.target.result
        var eee = _this.img
        console.log(_this.img)
        console.log(typeof eee)
        var arr = eee.split(','),
          mime = arr[0].match(/:(.*?);/)[1],
          bstr = atob(arr[1]),
          n = bstr.length,
          u8arr = new Uint8Array(n)
        while (n--) {
          u8arr[n] = bstr.charCodeAt(n)
        }
        var theBlob = new Blob([u8arr], { type: mime })
        theBlob.lastModifiedDate = new Date()
        theBlob.name = 'fileName'
        _this.Blob(theBlob)
      }
      reader.readAsDataURL(file)
    },
    Blob(theBlob) {
      this.blobb = theBlob
      console.log(this.blobb)
    }
  }
}
</script>
