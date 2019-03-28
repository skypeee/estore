<template>
    <div class="personal">
        <!-- 个人详情页 -->
        <!-- self_info -->
	<div class="grzxbj">
		<div class="selfinfo center">
		<div class="lfnav fl">
			<div class="ddzx">订单中心</div>
			<div class="subddzx">
				<ul><router-link to="order"><li><a >我的订单</a></li></router-link>
				</ul>
			</div>
			<div class="ddzx">个人中心</div>
			<div class="subddzx">
				<ul><router-link to="/personal"><li><a  style="color:#ff6700;font-weight:bold;">我的个人中心</a></li>
					</router-link>
					
				</ul>
			</div>
		</div>
		<div class="rtcont fr">
			<div class="grzlbt ml40">我的资料 <el-button style="margin-left:20px;" type="warning" icon="el-icon-edit" circle></el-button></div>   
			<div class="subgrzl ml40"><span>昵称</span><span>{{this.userlist.last_name}}</span></div>
			<div class="subgrzl ml40"><span>手机号</span><span>{{this.userlist.user_phone}}</span></div>
			<div class="subgrzl ml40"><span>密码</span><span>************</span></div>
			<div class="subgrzl ml40"><span>个性签名</span><span>一支穿云箭，千军万马来相见！</span></div>
			<div class="subgrzl ml40"><span>我的爱好</span><span>游戏，音乐，旅游，健身</span></div>
			<div class="subgrzl ml40"><span>收货地址</span><span>浙江省杭州市江干区19号大街571号</span></div>
			
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
  data(){
    return{
		username:'',
		userlist:[],
    }
  },
  created(){
	  this.findAll()
		},
		
  methods:{
    findAll(){
			 axios.post('/wish/api-token-verify/',{'token':Cookies.get('token')})
		.then((result)=>{
			console.log(result)
			this.username = result.data.user_id
			axios.get('/users/User_List/?search='+this.username)
				.then((result)=>{
					console.log(result)
					this.userlist = result.data.results[0]
				})
				.catch(()=>{
				console.log(this.token)
				})
				}).catch(()=>{
		console.log(this.token)
		})
	},
	 
  }
}
</script>
