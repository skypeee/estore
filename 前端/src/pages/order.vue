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
		<div class="rtcont fr" style="height:500px;overflow:scroll">
			<div  v-for="item in orderlist" >
				<div style="background-color: rgba(176,176,176,0.2);border-left: 5px solid #ff6700;font-size:12px;height:50px;line-height:25px;color:#00000;font-weight: bold;"> &emsp;&emsp;&emsp;订单时间:  {{formatDate(item.order_time)}}    &emsp;订单号:  {{item.order_time+item.order_num}} &emsp;&emsp;&emsp;总价：  {{item.max_price}}元  &emsp;&emsp;&emsp; 
					<br>&emsp;&emsp;&emsp;收货人：  {{item.order_aceptman}}  &emsp;&emsp;&emsp; 收获地址：  {{item.order_address}}  &emsp;&emsp;&emsp; 联系方式：  {{item.order_phone}}  &emsp;&emsp;&emsp; <span v-if="item.order_status">已付款</span><span v-else>未付款<el-button type="success" size="mini" icon = "el-icon-goods" circle @click="pay(item)" style="float:right;margin-right:20px;margin-top:-16px;" title="付款"></el-button></span>
				<el-button type="primary" size="mini" icon = "el-icon-edit" circle @click="Update(item)" style="float:right;margin-right:20px;margin-top:-16px;" title="修改收货人信息"></el-button>
				<el-button type="danger" size="mini" icon="el-icon-delete" circle @click="Delete(item.order_num)" style="float:right;margin-right:20px;margin-top:-16px;" title="取消订单"></el-button>
				<br></div>
				<el-table ref="multipleTable" :data="item.data" tooltip-effect="dark" style="width: 90%;margin-left:5%;" >
	<el-table-column
	  prop="good_img"
      label="商品图片"
      >
	  <template slot-scope="scope"><img :src="base+'media/'+scope.row.good_img" alt="" width="50px;" height="50px;"></template>
    </el-table-column>
		 
    <el-table-column
	  prop="good_name"
      label="商品名称"
     >
    </el-table-column>
    <el-table-column
      prop="good_price"
      label="单价"
      >
    </el-table-column>
    <el-table-column
      prop="good_num"
      label="数量"
      show-overflow-tooltip>
    </el-table-column>
	 <el-table-column
      label="小计"
      show-overflow-tooltip>
	  <template slot-scope="scope">{{scope.row.good_num * scope.row.good_price}}</template>
    </el-table-column>
	
  </el-table>
				<div class="clear"></div>
				
			</div>
			
		</div>
				<div class="page">
        <el-pagination background prev-text="上一页"  @current-change="handleCurrentChange2" next-text="下一页" layout="prev, pager, next" :total="total" :page-size=3 style="margin-top: 5px;float: right;margin-right: 15px;"></el-pagination>
      </div>
			
		<div class="clear"></div>
		</div>
	</div>
	<el-dialog
		title="修改收货人信息"
		:visible.sync="dialogVisible"
		width="30%"
		:before-close="handleClose">
	
			
		<el-form ref="form" :model="form" label-width="80px">
		
			<el-form-item
				label="收件人"
				prop="order_aceptman"
				label-text-align="center"
				>
				<el-input
					v-model="form.order_aceptman"
					size="mini"
					:placeholder="this.formdatd.order_aceptman"
				></el-input>
      </el-form-item>
		  <el-form-item label="手机号">
			<el-input v-model="form.order_phone" size="mini" :placeholder="this.formdatd.order_phone"></el-input>
			</el-form-item>
			
			</el-form-item>
			<el-form-item label="收货地址">
			<el-input v-model="form.order_address" size="mini" :placeholder="this.formdatd.order_address"></el-input>
			</el-form-item>

			 
			</el-form>	
		<span slot="footer" class="dialog-footer">

			<el-button @click="dialogVisible = false">取 消</el-button>
			<el-button type="primary" @click="queding(form)">确 定</el-button>
		</span>
	</el-dialog>
	
    </div>
</template>
<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
export default {
  data(){
    return{
		username:'',
		orderlist:[],
		total:6,
		form:{'order_aceptman':'','order_phone':'','order_address':''},
		formdatd:{},
		base:axios.defaults.baseURL,
		page:1,
		dialogVisible:false,
		
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
			axios.get('/goods/Order_List/?page='+this.page+'&page_size='+3+'&user_id='+this.username)
				.then((result)=>{
					console.log(result)
					this.total = result.data.count
					this.orderlist = result.data.result
				})
				.catch(()=>{
				console.log(this.token)
				})
				}).catch(()=>{
		console.log(this.token)
		})
	},
	handleCurrentChange2(val) {
	  this.page = val
	  console.log(this.page)
      this.findAll()
		},    
	formatDate(now) { 
		var Now=new Date(now); 
		var year=Now.getFullYear(); 
		var month=Now.getMonth()+1; 
		var date=Now.getDate(); 
		var hour=Now.getHours(); 
		var minute=Now.getMinutes(); 
		var second=Now.getSeconds(); 
		return year+"-"+month+"-"+date+" "+hour+":"+minute+":"+second; 
		},  
	 Delete(order_num){
		  axios.post('/goods/Order_Delete/',{'order_num':order_num})
		.then((result)=>{
			this.findAll()
			  this.$notify.success({
				  title: '删除订单成功',
				  message: '删除订单成功',
			  });
		})
		.catch((error)=>{
			  this.$notify.error({
				  title: '删除订单失败',
				  message: '删除订单失败',
			  })
		  })
	  },
	  Update(order){
		this.form={'order_aceptman':'','order_phone':'','order_address':''}
		this.formdatd = order
		// this.form['order_num'] = order.order_num
		// this.form['order_aceptman'] = order.order_aceptman
		// this.form['order_phone'] = order.order_phone
		// this.form['order_address'] = order.order_address
		this.dialogVisible = true

	  },
		handleClose(){
		  this.dialogVisible = false;
      if(this.$refs['form']!=undefined){
        this.$refs['form'].resetFields();
      }
      
	},
	queding(form){
		 this.form['order_num'] = this.formdatd.order_num
		 if (this.form['order_aceptman']==''){
			 this.form['order_aceptman'] = this.formdatd.order_aceptman
		 }
		 if (this.form['order_phone']==''){
			 this.form['order_phone'] = this.formdatd.order_phone
		 }
		 if (this.form['order_address'] == ''){
			 this.form['order_address'] = this.formdatd.order_address
		 }
		 axios.post('/goods/Order_Update/',this.form)
		.then((result)=>{
			this.findAll()
			  this.$notify.success({
				  title: '修改收货人信息成功',
				  message: '修改收货人信息成功',
			  });
		})
		.catch((error)=>{
			  this.$notify.error({
				  title: '修改收货人信息失败',
				  message: '修改收货人信息失败',
			  })
		  })
	},
	pay(order){
		 axios.post('/goods/ali_Pay/',{'order_num':order.order_num,'max_price':order.max_price})
		.then((result)=>{
			this.findAll()
			console.log(result.data.url)
			window.open(result.data.url)
			
		})
		.catch((error)=>{
			  this.$notify.error({
				  title: '跳转失败',
				  message: '请检查网络哦',
			  })
		  })

	}
	 
  }
}
</script>