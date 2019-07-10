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
			<div class="grzlbt ml40">我的资料 <el-button style="margin-left:20px;" type="warning" icon="el-icon-edit" circle @click="insertuser"></el-button></div>   
			<div class="subgrzl ml40"><span>昵称</span><span>{{this.userlist.last_name}}</span></div>
			<div class="subgrzl ml40"><span>手机号</span><span>{{this.userlist.user_phone}}</span></div>
			<div class="subgrzl ml40"><span>个性签名</span><span>{{this.userlist.user_signature}}</span></div>
			<div class="subgrzl ml40"><span>收货地址</span><span>{{this.userlist.user_address}}</span></div>
			
				<el-dialog
		title="修改个人信息"
		:visible.sync="dialogVisible"
		width="30%"
		:before-close="handleClose">
			
		<el-form ref="form" :model="form" label-width="80px">

			<el-form-item
				label="昵称"
				prop="last_name"
				label-text-align="center"
				>
				<el-input
					v-model="form.last_name"
					size="mini"
					placeholder="请输入用户名"
				></el-input>
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
		dialogVisible: false,
		form:{
		}
    }
  },
  created(){
	  this.findAll()
		},
		
  methods:{
    findAll(){
			 axios.post('/wish/api-token-verify/',{'token':Cookies.get('token')})
		.then((result)=>{
			this.username = result.data.user_id
			axios.get('/users/User_List/?search='+this.username)
				.then((result)=>{
					console.log(result)
					this.userlist = result.data[0]
					console.log(this.userlist)
				})
				.catch(()=>{
				})
				}).catch(()=>{
		})
	},
	insertuser(){
		this.dialogVisible = true
		this.form = this.userlist
		delete this.form["password"]
	},
	insertok(form){

		this.dialogVisible = false
		axios.post("/users/User_Updated/", this.form).then((result)=>{
			this.$notify.success({
                    title: "成功",
                    message: "修改个人信息成功"
                  });
		}).catch(error => {
                  this.findAll();
                  this.$notify.error({
                    title: "网络链接错误",
                    message: "加载数据失败"
                  });
                });
	},
	handleClose(){
		  this.dialogVisible = false;
      if(this.$refs['form']!=undefined){
        this.$refs['form'].resetFields();
      }
      this.form = {};
      this.findAll()
      
	}

	}
	
}
</script>
