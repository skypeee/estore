<template>
  <div id="login">
    <div class="top center">
      <div class="logo center"></div>
    </div>
    <div class="form center">
      <div class="login">
        <div class="login_center">
          <div class="login_top">
            <div class="left fl">会员登录</div>
            <div class="right fr">
              您还不是我们的会员？
              <a target="_self" @click="register">立即注册</a>
              <a @click="index" target="_self">主页</a>
            </div>
            <div class="clear"></div>
            <div class="xian center"></div>
          </div>
          <div class="login_main center">
            <div class="username">
              用户名:&nbsp;
              <input
                class="shurukuang"
                type="text"
                name="username"
                placeholder="请输入你的用户名"
                v-model="username"
              />
            </div>
            <div class="username">
              密&nbsp;&nbsp;&nbsp;&nbsp;码:&nbsp;
              <input
                class="shurukuang"
                type="password"
                name="password"
                placeholder="请输入你的密码"
                v-model="password"
                @keyup.enter="login"
              />
            </div>
            <!-- <div class="username">
						<div class="left fl">验证码:&nbsp;<input class="yanzhengma" type="text" name="username" placeholder="请输入验证码"/></div>
						<div class="right fl"><img src="./image/yanzhengma.jpg"></div>
						<div class="clear"></div>
            </div>-->
          </div>
          <div class="login_submit">
            <input class="submit" name="submit" value="          立即登录" @click="login" />
          </div>
        </div>
      </div>
    </div>
    <footer>
      <div class="copyright">简体 | 繁体 | English | 常见问题</div>
      <div class="copyright">
        版权所有-京ICP备10046444-
        <img src="./image/ghs.png" alt />京公网安备11010802020134号-京ICP证110507号
      </div>
    </footer>
  </div>
</template>

<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
// headers:{'Authorization':this.token},

export default {
  data() {
    return {
      username: '',
      password: '',
      form: {},
      token: 'JWT ' + Cookies.get('token')
    }
  },
  created() {
    console.log(Cookies.get('token'))
    axios
      .post('/wish/api-token-verify/', { token: Cookies.get('token') })
      .then(result => {
        console.log(result)
        console.log('ok')
      })
      .catch(() => {
        console.log(this.token)
      })
    // var _self = this;
    //     document.onkeydown = function(e){
    //         var key = window.event.keyCode;
    //         if(key == 13){
    //             _self.login();
    // 		}
    // 	}
  },
  methods: {
    register() {
      this.$root.currentComponent = 'register'
    },
    index() {
      this.$root.currentComponent = 'App'
    },
    login() {
      axios
        .post('/users/api-token-auth/', {
          username: this.username,
          password: this.password
        })
        .then(result => {
          Cookies.set('token', result.data.token, { expires: 0.1 })
          this.token = 'JWT ' + result.data.token
          console.log(Cookies.get('token'))
          ;(this.$root.currentComponent = 'App'),
            this.$notify.success({
              title: '登陆成功',
              message: '登陆成功'
            })
        })
        .catch(error => {
          this.$notify.error({
            title: '登陆失败',
            message: '登陆失败'
          })
        })
    }
  }
}
</script>

<style scoped>
/*样式初始化*/
* {
  margin: 0;
  padding: 0;
}
a {
  text-decoration: none;
  color: #000;
  cursor: pointer;
}
img {
  border: 0;
  vertical-align: middle;
}
ul li {
  list-style: none;
}
body,
h1,
h2,
h3,
h4,
h5,
h6 {
  font: 12px 宋体, Times New Roman;
}

/*预定义样式*/
.w {
  width: 1000px;
  margin: 0 auto;
}
.fl {
  float: left;
}
.fr {
  float: right;
}
.clear {
  clear: both;
}
.center {
  margin: 0 auto;
}
.border {
  border: 1px solid red;
}

table {
  width: 360px;
  height: 240px;
  border: none;
  margin: 0 auto;
}
tr,
th,
td {
  height: 20px;
}
th {
  width: 60px;
}
input:focus {
  border: 2px solid orange;
}
/*用户登录*/
.top {
  width: 100%;
  height: 100px;
  background: #fff;
}
.top .logo {
  width: 1130px;
  height: 100px;
}
.form {
  width: 100%;
  height: 450px;
  background: url('./image/222.png') 110px 0px no-repeat;
  background-color: rgb(247, 247, 255);
}
.login {
  width: 400px;
  height: 470px; /*border:1px solid #ff6700;*/
  margin: 30px auto;
  background: #444;
  color: #fff;
  margin-right: 100px;
  border-radius: 4px;
}
.login .login_center {
  width: 360px;
  margin: 30px auto;
}
.login .login_top {
  margin: 10px 0;
}
.login .login_top .left {
  height: 40px;
  line-height: 40px;
  font-weight: bold;
  font-size: 20px;
}
.login .login_top .right {
  height: 40px;
  line-height: 40px;
  font-size: 13px;
}
.login .login_top .right a {
  color: red;
  font-weight: bold;
}
.login .login_top .right a:hover {
  color: orange;
}
.xian {
  height: 2px;
  background: #ff6700;
  margin: 8px 0;
}

.login_main {
  padding: 20px 0;
}
.login_main .username {
  font: 16px Times New Roman;
  height: 40px;
  line-height: 40px;
  margin: 35px 0;
}
.login_main .username .shurukuang {
  width: 220px;
  height: 30px;
  border: 1px solid #ccc;
  padding: 5px 10px;
}
.login_main .username .yanzhengma {
  width: 100px;
  height: 30px;
  border: 1px solid #ccc;
  padding: 5px 10px;
}
.login_main .username .shurukuang:focus {
  border: 1px solid blue;
  background: #f0ffff;
}
.login_main .username .yanzhengma:focus {
  border: 1px solid blue;
  background: #f0ffff;
}
.login_main .username .right {
  margin-left: 20px;
}

/*设置按钮样式*/
.login .login_center .login_submit {
  margin: 15px auto;
}
.login .login_center .submit {
  border: none;
  width: 240px;
  height: 45px;
  margin-left: 55px;
  background: #ff6700;
  color: #fff;
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 2px;
  cursor: pointer;
  border-radius: 4px;
}
.login .login_center .submit:hover {
  border: 1px solid #fff;
}

footer {
  width: 100%;
  height: 80px;
  background: #fff;
  padding: 30px 0;
}
footer .copyright {
  height: 30px;
  line-height: 30px;
  font-size: 13px;
  word-spacing: 15px;
  text-align: center;
}
footer .copyright:first-of-type {
  margin-top: 10px;
}
</style>
