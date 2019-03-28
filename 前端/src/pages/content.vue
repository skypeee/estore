<template>
    <div class="content">
        <!-- 内容详情页面 -->
        <!-- xiangqing -->
	<div class="xiangqing">
		<div class="neirong w">
			<div class="xiaomi6 fl">{{this.content.good_name}}</div>
			<nav class="fr">
				<li><a  >概述</a></li>
				<li>|</li>
				<li><a  >变焦双摄</a></li>
				<li>|</li>
				<li><a  >设计</a></li>
				<li>|</li>
				<li><a  >参数</a></li>
				<li>|</li>
				<li><a  >F码通道</a></li>
				<li>|</li>
				<li><a  >用户评价</a></li>
				<div class="clear"></div>
			</nav>
			<div class="clear"></div>
		</div>	
	</div>
	
	<div class="jieshao mt20 w">
		<div class="left fl"><img :src="this.content.good_img"></div>
		<div class="right fr">
			<div class="h3 ml20 mt20">{{this.content.good_name}}</div>
			<div class="jianjie mr40 ml20 mt10">{{this.content.good_content}}</div>
			<div class="jiage ml20 mt10">{{this.content.good_price}}元</div>
			<div class="ft20 ml20 mt20">选择版本</div>
			<div class="xzbb ml20 mt10">
				<div class="banben fl">
					<a>
						{{this.content.good_parameter}} 
					
					</a>
				</div>
				
				<div class="clear"></div>
			</div>
			<div class="ft20 ml20 mt20">选择颜色</div>
			<div class="xzbb ml20 mt10">
				<div class="banben">
					<a>
						<span class="yuandian"></span>
						<span class="yanse">{{this.color}}</span>
					</a>
				</div>
				
			</div>
			<div class="xqxq mt20 ml20">
				<div class="top1 mt10">
					<div class="left1 fl">{{this.content.good_name}}    {{this.content.good_parameter}}    {{this.color}}</div>
					<div class="right1 fr">{{this.content.good_price}}元</div>
					<div class="clear"></div>
				</div>
				<div class="bot mt20 ft20 ftbc">总计：{{this.content.good_price}}元</div>
			</div>
			<div class="xiadan ml20 mt20">
					
					<input class="jrgwc" type="button" name="jrgwc" value="加入购物车" @click="buy"/>
				
			</div>
		</div>
		<div class="clear"></div>
	</div>
    </div>
</template>
<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
export default {
  data(){
    return{
		id:'',
		content:{},
		color:'',
		username:0,
    }
  },
  created(){
	  this.findAll()
	  axios.post('/wish/api-token-verify/',{'token':Cookies.get('token')})
		.then((result)=>{
			this.login = "注销"
			this.username = result.data.user_id
		console.log('ok')
		}).catch(()=>{
			this.$notify.error({
				  title: '请登录',
				  message: '请登录',
			  })
		console.log(this.token)
		})
    },
  methods:{
    findAll(){
        this.id = this.$route.query.id
        axios.get('/goods/Good_list/?search='+this.id)
        .then((result)=>{
			this.content = result.data.results[0]
			if(this.content.good_color==1){
				this.color = '红色'
			}
			if(this.content.good_color==2){
				this.color = '亮黑色'
			}
			if(this.content.good_color==1){
				this.color = '玫瑰金'
			}

        })
	},
	buy(){
		var id = Number(this.id)
		console.log(this.username)
		if(this.username == 0){
				this.$notify.error({
				  title: '请登录',
				  message: '请登录',
			  })
		}
		else{
			axios.post('/goods/Favorite_Create/',{"good_num":1,"good":id,"user":this.username})
			.then((result)=>{
				console.log(result)
				this.$router.push({path:'/shopping',})
					this.$notify.success({
						title: '加入购物车成功',
						message: '加入购物车成功',
					});
			})
			.catch((error)=>{
					this.$notify.error({
						title: '加入购物车失败',
						message: '加入购物车失败',
					})
				})
			}
		
	}
  }
}
</script>