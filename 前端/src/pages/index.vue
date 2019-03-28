<template>
    <div class="index">
        <!-- 主页页面 -->
		 <!-- start banner_x -->
                <div class="banner_x center">
				
                    <a  ><div class="ad_top fl"></div></a>
                    <div class="nav fl">
                        <ul>
                            <li ><a @click="contentlistlink('手机')">手机</a></li>
                            <li><a  @click="contentlistlink('平板.笔记本')">平板.笔记本</a></li>
                            <li><a   @click="contentlistlink('电视')">电视</a></li>
                            <li><a   @click="contentlistlink('平板.笔记本')">路由器</a></li>
                            <li><a   @click="contentlistlink('耳机')">耳机</a></li>
							<li><a   @click="contentlistlink('音箱')">音响</a></li>
							<li><a   @click="contentlistlink('')">所有商品</a></li>

							
                        </ul>
                    </div>
                  
                </div>
        <!-- end banner_x -->
        <!-- start banner_y -->
		<div class="banner_y center">
			<div class="nav">				
				<ul>
					<li>
						<a  >手机</a>
						<div class="pop">
							<div class="left fl" >
								<div v-for="item in goodslist">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt="" width=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a   >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="ctn fl">
								<div v-for="item in goodslist2">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a  >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="clear"></div>
						</div>
					</li>
					<li>
						<a  >笔记本</a>
						<a  >平板</a>
						<div class="pop">
							<div class="left fl">
								<div v-for="item in goodslist3">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt="" width=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a   >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="ctn fl">
								<div v-for="item in goodslist4">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a  >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="clear"></div>
						</div>
					</li>
					<li>
						<a  >电视</a>
						<div class="pop">
							<div class="left fl">
								<div v-for="item in goodslist5">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt="" width=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a   >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							
							<div class="clear"></div>
						</div>
					</li>
					<li>
						<a  >路由器</a>
						<div class="pop">
							<div class="left fl">
								<div v-for="item in goodslist6">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt="" width=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a   >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="ctn fl">
								<div v-for="item in goodslist7">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt=""></div>
											<span class="fl">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a  >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="clear"></div>
						</div>
					</li>
					
					<li>
						<a  >耳机</a>
					
						<div class="pop">
							<div class="left fl">
								<div v-for="item in goodslist8">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt="" width=""></div>
											<span class="fl" style="width:100px;overflower:hidden">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a   >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="ctn fl">
								<div v-for="item in goodslist9">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt=""></div>
											<span class="fl" style="overflower:hidden">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a  >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="clear"></div>
						</div>
					</li>
					
					<li>
						<a  >音响</a>
						<div class="pop">
							<div class="left fl">
								<div v-for="item in goodslist10">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt="" width=""></div>
											<span class="fl" style="width:100px;overflower:hidden">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a   >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="ctn fl">
								<div v-for="item in goodslist11">
									<div class="xuangou_left fl">
										<a  >
											<div class="img fl"><img :src="item.good_img" alt=""></div>
											<span class="fl" style="overflower:hidden">{{item.good_name}}</span>
											<div class="clear"></div>
										</a>
									</div>
									<div class="xuangou_right fr"  @click="contentlink(item.id)"><a  >选购</a></div>
									<div class="clear"></div>
								</div>
							</div>
							<div class="clear"></div>
						</div>
					</li>
				</ul>
			</div>
		</div>	
		
	<!-- start danpin -->
		<div class="danpin center">
			
			<div class="biaoti center">手机</div>
			<div class="main center" >
				<div class="mingxing fl" v-for='item in goodslist' @click="contentlink(item.id)">
					<div class="sub_mingxing"><a  ><img :src="item.good_img" alt=""></a></div>
					<div class="pinpai"><a  >{{item.good_name}}</a></div>
					<div class="youhui">{{item.good_content}}</div>
					<div class="jiage">{{item.good_price}}元起</div>
				</div>
				<div class="clear"></div>
			</div>
		</div>
		<div></div>
		<div class="danpin center">
			<div class="biaoti center">耳机</div>
			<div class="main center" >
				<div class="mingxing fl" v-for='item in goodslist8' @click="contentlink(item.id)">
					<div class="sub_mingxing"><a  ><img :src="item.good_img" alt=""></a></div>
					<div class="pinpai"><a  >{{item.good_name}}</a></div>
					<div class="youhui">{{item.good_content}}</div>
					<div class="jiage">{{item.good_price}}元起</div>
				</div>
				<div class="clear"></div>
			</div>
		</div>
		<div></div>
		<div class="danpin center">
			<div class="biaoti center">笔记本</div>
			<div class="main center" >
				<div class="mingxing fl" v-for='item in goodslist3' @click="contentlink(item.id)">
					<div class="sub_mingxing"><a  ><img :src="item.good_img" alt=""></a></div>
					<div class="pinpai"><a  >{{item.good_name}}</a></div>
					<div class="youhui">{{item.good_content}}</div>
					<div class="jiage">{{item.good_price}}元起</div>
				</div>
				<div class="clear"></div>
			</div>
		</div>
		<div></div>
		
		
    </div>
</template>
<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
export default {
	data(){
		return{
			goodslist:[],
			goodslist2:[],
			goodslist3:[],
			goodslist4:[],
			goodslist5:[],
			goodslist6:[],
			goodslist7:[],
			goodslist8:[],
			goodslist9:[],
			goodslist10:[],
			goodslist11:[],
		}
	},
	created(){
		this.findall()
	},
	methods:{
		findall(){
			axios.get('/goods/Good_list/?search=手机')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist = result.data.results
			})
			axios.get('/goods/Good_list/?page=2&search=手机')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist2 = result.data.results
			})
			axios.get('/goods/Good_list/?search=平板.笔记本')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist3 = result.data.results
			})
			axios.get('/goods/Good_list/?page=2&search=平板.笔记本')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist4= result.data.results
			})
			axios.get('/goods/Good_list/?search=电视')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist5 = result.data.results
			})
			axios.get('/goods/Good_list/?search=路由器')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist6 = result.data.results
			})
			axios.get('/goods/Good_list/?page=2&search=路由器')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist7= result.data.results
			})
			axios.get('/goods/Good_list/?search=耳机')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist8 = result.data.results
			})
			axios.get('/goods/Good_list/?page=2&search=耳机')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist9= result.data.results
			})
			axios.get('/goods/Good_list/?search=音响')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist10 = result.data.results
			})
			axios.get('/goods/Good_list/?page=2&search=音响')
			.then((result)=>{
				console.log(result.data.results)
				this.goodslist11= result.data.results
			})
		
		},
		 contentlistlink(name){
		    this.$router.push({path:'/contentList',query:{id:name}})
	  },
	  contentlink(id){
		    this.$router.push({path:'/content',query:{id:id}})
	  }
	}
}
</script>

