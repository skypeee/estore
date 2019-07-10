<template>
    <div class="content">
        <!-- 内容详情页面 -->
        <!-- xiangqing -->
	<div class="xiangqing">
		<div class="neirong w">
			<div class="xiaomi6 fl">{{this.content.good_name}}</div>
			<nav class="fr">
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
				<div class="response" style="margin:30px;">
					
							<h4>评论</h4>
							
							<div class="media response-info" v-for="item,index in commentlist" style="border: 1px dotted #CDCCCC;padding:5px;">
								
								<div class="media-left response-text-left"  >
									<h5 style="color:#F81800">第<span style="margin:2px;color:#9ae50c;">{{index+1}}</span>楼</h5>

									<h5>{{item.user.last_name}}</h5>
									
								</div>
								<div class="media-body response-text-right">
									<p v-html="item.comment_content" style="margin-top:10px;text-align:left;margin-left:15%;"><a>{{item.comment_content}}</a></p>
									<ul>
										<li>{{item.comment_time}}</li>
										
									</ul>
									</div>
								</div>
								<div class="clearfix"> </div>
								<p style="color:red;text-align:left;margin:20px;cursor:pointer;" @click="commentcreat">发表你的评论</p>
							</div>
				<div class="Dialog">
										<el-dialog title="发表评论" :visible.sync="dialogFormVisible" :before-close="closeFormDialog" top="10px" >
											<el-form :model="form"  ref="form" class="demo-ruleForm">
												<el-form-item
													label="用户昵称"
													prop="username"
													:label-width="formLabelWidth"
													label-text-align="center"
												>
													<el-input
													disabled
														v-model="form.username"
														size="mini"
													></el-input>
												</el-form-item>
											
													<label>评论</label>
													
													<div id="editor1" style="height:400px;max-height:300px;"></div>
											</el-form>
											<div slot="footer" class="dialog-footer">
												<el-button size="small" type="primary"  @click="Addarticle('form')">确 定</el-button>
												
											</div>
								</el-dialog>
							</div>
    </div>
</template>
<script>
import axios from '@/http/axios'
import Cookies from 'js-cookie'
import E from 'wangeditor'
export default {
  data(){
    return{
		id:'',
		content:{},
		color:'',
		username:0,
		Username:'',
		commentlist:[],
		form:{},
		formLabelWidth:"500px;",
		dialogFormVisible:false,
    }
  },
  created(){
	  this.findAll()
	  axios.post('/wish/api-token-verify/',{'token':Cookies.get('token')})
		.then((result)=>{
			this.login = "注销"
			this.username = result.data.user_id
			this.Username = result.data.last_name
				
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
        axios.get('/goods/Good_list/?id='+this.id)
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
				axios.get('goods/Comment_List/?good_id='+this.id)
				.then((result)=>{
					console.log(result)
					this.commentlist = result.data.results
				})

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
		
	},
	closeFormDialog() {
            this.dialogFormVisible = false;
            if (this.$refs['form']!=undefined){
                this.$refs['form'].resetFields();
            }
            this.findAll()
            },
		commentcreat(){
		if(this.username!=0){
				this.form={'username':this.Username,'user':this.username,'good':this.id}
				this.dialogFormVisible=true
				
		}
		else{
			alert('请先登陆')
		}
	
		this.$nextTick(function() {this.editor = new E('#editor1')
				this.editor.customConfig.uploadImgShowBase64=true;
        this.editor.customConfig.uploadImgMaxSize = 3 * 1024 * 1024;
        this.editor.customConfig.uploadImgMaxLength = 5;
		    this.editor.customConfig.menus = [
       'head',
        'bold',
        'italic',
				'underline',
				'justify',//对齐方式
             'foreColor',  // 文字颜色
    'backColor',  // 背景颜色
    'link',  // 插入链接
              'emoticon',  // 表情
    'image',  // 插入图片
             'undo',  // 撤销
    'redo'  // 重复
     ];
		this.editor.create();
    this.editor.txt.clear()
		})

		
	},
	Addarticle(form){
		this.dialogFormVisible = false;
				var formData = new FormData();
				 formData.append("good", this.form.good);
        formData.append("user", this.form.user);
        formData.append("comment_content", this.editor.txt.html());
        var options = {
        url: "/goods/Comment_Created/",
        data: formData,
        method: "post",
        contentType: false,
        headers: { "Content-Type": "multipart/form-data" }
        };
              axios(options)
                .then(result => {
                  this.$notify.success({
                    title: "成功",
                    message: "评论成功"
                  });
                  this.findAll();
                  this.$refs[form].clearValidate();
                })
	},
  }
}
</script>