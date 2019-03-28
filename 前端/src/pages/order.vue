<template>
    <div class="order">
        <!-- 订单页面 -->
        <!-- self_info -->
	<div class="grzxbj">
		<div class="selfinfo center">
		<div class="lfnav fl">
			<div class="ddzx">订单中心</div>
			<div class="subddzx">
				<ul><router-link to="order"><li><a  style="color:#ff6700;font-weight:bold;">我的订单</a></li></router-link>
				</ul>
			</div>
			<div class="ddzx">个人中心</div>
			<div class="subddzx">
				<ul><router-link to="/personal"><li><a >我的个人中心</a></li>
					</router-link>
					
				</ul>
			</div>
		</div>
		<div class="rtcont fr">
			<div class="ddzxbt">交易订单</div>
			<div class="ddxq" v-for="item in userlist">
				<div class="ddspt fl"><img :src="item.good.good_img" alt="" width="70px;" height="80px;"></div>
				<div class="ddbh fl">订单号:{{item.id}}</div>
				<div class="ztxx fr">
					<ul>
						<li>已发货</li>
						<li>单价 {{item.good.good_price}} 元</li>
						<li>{{item.good_num}}件</li>
						
						<li>￥{{item.good_num * item.good.good_price}}</li>
						
						<div class="clear"></div>
					</ul>
				</div>
				<div class="clear"></div>
			</div>
			
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
			console.log(this.username)
			axios.get('/goods/Order_List/?search='+this.username)
				.then((result)=>{
					console.log(result)
					this.userlist = result.data.results
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