<template>
    <div class="regist">
        <div class="regist_center">
				<div class="regist_top">
					<div class="left fl">会员注册</div>
					<div class="right fr"><a  target="_self" @click="login">立即登陆    </a><a @click="index" target="_self">主页</a></div>
					<div class="clear"></div>
					<div class="xian center"></div>
				</div>
				<div class="regist_main center">
					<div class="username">用&nbsp;&nbsp;户&nbsp;&nbsp;名:&nbsp;&nbsp;<input class="shurukuang" type="text" name="username" placeholder="请输入你的用户名" v-model="last_name"/><p>请不要输入汉字</p></div>
					<div class="username">密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码:&nbsp;&nbsp;<input class="shurukuang" type="password" name="password" placeholder="请输入你的密码" v-model="password"/><p>请输入6位以上字符</p></div>
					
					<div class="username">确认密码:&nbsp;&nbsp;<input class="shurukuang" type="password" name="repassword" placeholder="请确认你的密码" :model="re_password"/><p>两次密码要输入一致哦</p></div>
					<div class="username">手&nbsp;&nbsp;机&nbsp;&nbsp;号:&nbsp;&nbsp;<input class="shurukuang" type="text" name="tel" placeholder="请填写正确的手机号" v-model="phone_num"/><el-button plain class="CAPTCHA" @click="captcha">获取验证码</el-button></div>
					<div class="username">
						<div class="left fl">验&nbsp;&nbsp;证&nbsp;&nbsp;码:&nbsp;&nbsp;<input class="yanzhengma" type="text" name="username" placeholder="请输入验证码" v-model="re_captcha"/></div>
						<div class="clear"></div>
					</div>
				</div>
				<div class="regist_submit">
					<input class="submit"  name="submit" value="            立即注册" @click="register" >
				</div>
				
			</div>
    </div>
</template>
<script>
import axios from '@/http/axios'
export default {
  data(){
	  return{
			phone_num: '',
			captcha_num: '',
			last_name:'',
			password: '',
			re_password: '',
			re_captcha: '',
	  }
  },
  methods:{
	  login(){
		  this.$root.currentComponent = 'login'
		},
		index(){
			this.$root.currentComponent = 'App'
		},
		captcha(){
				axios.post('/users/message_send/', {'phone_num':this.phone_num})
				.then((result)=>{
					this.captcha_num=result.data.CAPTCHA
					console.log(this.captcha_num)
					})
				.catch((error)=>{
					this.$notify.error({
						title:'网络连接错误',
						message: '加载数据失败',
					});
				});
			},
			register(){
				if(this.captcha_num==this.re_captcha && this.password==this.re_password){
					axios.post('/users/User_Created/', {'username': this.last_name,'last_name': this.last_name, 'password': this.password, 'user_phone': this.phone_num})
				.then((result)=>{
					this.$notify.success({
						title:'注册成功',
						message: '注册用户成功',
					});
					this.$root.currentComponent = 'login'
					})
					.catch((error)=>{
					this.$notify.error({
						title:'网络连接错误',
						message: '注册用户失败',
					});
				})
				}
				else if(this.captcha_num!=this.re_captcha){
				   this.$notify.error({
						title:'验证码',
						message: '验证码错误',
					});
				}
				else{
						this.$notify.error({
						title:'密码错误',
						message: '两次密码输入不统一',
					});
				}
		},
  }
}
</script>

<style scoped>
.CAPTCHA_a{
	font-size: 12px;
	margin-left: 20px;
}
.CAPTCHA {
	width: 150px;
	height: 30px;
	margin-left: 20px;
	font-size: 12px;
	color: #ccc;
	font-weight: bold;
}
/*样式初始化*/
*{margin:0;padding: 0;}
a{text-decoration: none;color: #000;cursor: pointer;}
img {border: 0; vertical-align:middle;} 
ul li{list-style: none;}
body,h1,h2,h3,h4,h5,h6{font: 12px 宋体,Times New Roman;}

#regist{background: rgb(20,33,42)  }
/*预定义样式*/
.w{width: 1000px;margin: 0 auto;}
.fl{float: left;}
.fr{float: right;}
.clear{clear:both;}
.center{margin:0 auto;}
.border{border:1px solid red;}

table{width: 360px;height: 240px;border:none;margin: 0 auto;}
tr,th,td{height: 20px;}
th{width: 60px;}
input:focus{border: 2px solid orange;}

/*用户注册*/
.regist{width: 100%;height: 550px;margin:20px auto;background:#fff;color:#000;border-radius: 6px;margin-top: 100px;background:rgba(71, 70, 70,0.8) }
.regist_center{width: 760px;margin: 10px auto;}
.regist .regist_top{margin: 10px 0;}
.regist .regist_top .left{height: 40px;line-height: 40px;font-weight: bold;font-size: 20px;}
.regist .regist_top .right{height: 40px;line-height: 40px;font-size: 13px;}
.regist .regist_top .right a{color:#ff6700;font-weight: bold;}
.regist .regist_top .right a:hover{color:orange;}
.xian{height: 2px;background: #ff6700;margin: 8px auto;}

.regist_main{padding:10px 0;padding-left:45px;}
.regist_main .username{font:16px Times New Roman;height: 40px;line-height: 40px;margin:20px 0;}
.regist_main .username .shurukuang{width: 220px;height: 30px;border:1px solid #ccc;padding:5px 10px; }
.regist_main .username .yanzhengma{width: 100px;height: 30px;border:1px solid #ccc;padding:5px 10px; }
.regist_main .username .shurukuang:focus{border: 1px solid blue;background: #F0FFFF;}
.regist_main .username .yanzhengma:focus{border: 1px solid blue;background: #F0FFFF;}
.regist_main .username .right{margin-left: 20px;}

.regist_main .username p{display:inline-block;margin-left:20px;font-size: 12px;color: #ccc;font-weight: bold;}
.regist_main .username p:hover{color: #409eff;}

.regist .regist_center .regist_submit{margin: 20px auto;}
.regist .regist_center .submit{border:none;width: 440px;height: 45px;margin-left:45px;background: #ff6700;color: #fff; font-size: 22px;font-weight: bold;letter-spacing: 8px;cursor:pointer;}
.regist .regist_center .submit:hover{border:1px solid #ccc;}

footer{width: 100%;height: 80px;background:#fff;padding: 30px 0;}
footer .copyright{height: 30px;line-height: 30px;font-size: 13px;word-spacing: 15px;text-align: center;}
footer .copyright:first-of-type{margin-top: 10px;}


</style>
