<template>
  <div class="Super">
    <br />
    <h1 style="margin-left:20px;float:left">商品管理</h1>
    <div style="margin-top: 10px;">
      <el-button
        plain
        size="small"
        style="background-color: #1AA094;border-radius:4px;color: #ffffff;margin-right: 30px;margin: 11px;height:30px;float:right"
        class="addbtn"
        @click="addbtndialog"
      >新增商品</el-button>
      <el-input
        v-model="susuo"
        size="mini"
        placeholder="请输入内容"
        style="width:300px;margin-left:1000px;margin:10px;float:right"
        @change="search"
      ></el-input>
      <el-table
        class="El-table"
        :data="tableData"
        border
        :header-cell-style="{background:'#ff67007d'}"
        height="500px"
        size="mini"
        @current-change="handleCurrentChange"
        style="width:98%;margin-left: 10px;"
        v-loading="loading"
      >
        <el-table-column label="序号" type="index" header-align="center" align="center"></el-table-column>
        <el-table-column prop="good_name" label="商品名称" header-align="center" align="center"></el-table-column>
        <el-table-column prop="good_price" label="商品价格" header-align="center" align="center"></el-table-column>
        <el-table-column prop="good_num" label="商品库存" header-align="center" align="center"></el-table-column>
        <el-table-column prop="good_type" label="商品归类" header-align="center" align="center"></el-table-column>
        <el-table-column prop="good_parameter" label="商品描述" header-align="center" align="center"></el-table-column>
        <el-table-column prop="good_brand" label="商品品牌" header-align="center" align="center"></el-table-column>

        <el-table-column
          prop="Operation"
          label="操作"
          width="150px"
          header-align="center"
          align="center"
        >
          <template slot-scope="scope">
            <el-button
              type="primary"
              title="修改"
              icon="el-icon-edit"
              style="width: 30px;height: 30px;background-color:#1AA094;padding: 0px"
              @click="ExitMaterial(scope.row)"
            ></el-button>
            <!-- <el-button
              type="danger"
              title="删除"
              icon="el-icon-delete"
              style="width: 30px;height: 30px;padding: 0px"
              @click="DeleteMaterial(scope.row)"
            ></el-button>-->
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="page" style="height:50px;">
      <el-pagination
        background
        prev-text="上一页"
        @current-change="handleCurrentChange2"
        next-text="下一页"
        layout="prev, pager, next"
        :total="total"
        :page-size="10"
        style="margin-top: 25px;float: right;margin-right: 15px;"
      ></el-pagination>
    </div>
    <div class="Dialog">
      <el-dialog
        title="新增商品"
        :visible.sync="dialogFormVisible"
        :before-close="closeFormDialog"
        top="100px"
      >
        <el-form :model="form" ref="form" class="demo-ruleForm">
          <el-form-item
            label="商品名称"
            prop="good_name"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form.good_name"
              size="mini"
              placeholder="请输入商品名称"
              style="width: 400px"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品价格"
            prop="good_price"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input-number v-model="form.good_price" :step="100" :min="0"></el-input-number>
          </el-form-item>
          <el-form-item
            label="商品库存"
            prop="good_num"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input-number v-model="form.good_num" :step="100" :min="0"></el-input-number>
          </el-form-item>
          <el-form-item
            label="商品关键字"
            prop="good_content"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form.good_content"
              placeholder="请输入商品关键字"
              size="mini"
              style="width: 400px;"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品描述"
            prop="good_parameter"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form.good_parameter"
              placeholder="请输入商品描述"
              size="mini"
              style="width: 400px;"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品品牌"
            prop="good_brand"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form.good_brand"
              placeholder="请输入商品品牌"
              size="mini"
              style="width: 400px;"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品归类"
            prop="good_type"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-select v-model="form.good_type" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.label"
                :label="item.label"
                :value="item.label"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item
            label="商品图片："
            prop="good_img"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-upload
              class="avatar-uploader"
              action="123"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :on-change="onchange"
              :before-upload="beforeAvatarUpload"
            >
              <img v-if="imageUrl" :src="imageUrl" class="avatar" style="width:100px;height:100px;" />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button size="small" type="primary" @click="AddUser('form')">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <div class="Dialog">
      <el-dialog
        title="修改商品"
        :visible.sync="dialogFormVisible2"
        :before-close="closeForm2Dialog"
        top="100px"
      >
        <el-form :model="form2" ref="form2" class="demo-ruleForm">
          <el-form-item
            label="商品名称"
            prop="good_name"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form2.good_name"
              size="mini"
              placeholder="请输入商品名称"
              style="width: 400px"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品价格"
            prop="good_price"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input-number v-model="form2.good_price" :step="100" :min="0"></el-input-number>
          </el-form-item>
          <el-form-item
            label="商品库存"
            prop="good_num"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input-number v-model="form2.good_num" :step="100" :min="0"></el-input-number>
          </el-form-item>
          <el-form-item
            label="商品关键字"
            prop="good_content"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form2.good_content"
              placeholder="请输入商品关键字"
              size="mini"
              style="width: 400px;"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品描述"
            prop="good_parameter"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form2.good_parameter"
              placeholder="请输入商品描述"
              size="mini"
              style="width: 400px;"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品品牌"
            prop="good_brand"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-input
              v-model="form2.good_brand"
              placeholder="请输入商品品牌"
              size="mini"
              style="width: 400px;"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="商品归类"
            prop="good_type"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-select v-model="form2.good_type" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.label"
                :label="item.label"
                :value="item.label"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item
            label="商品图片："
            prop="good_img"
            :label-width="formLabelWidth"
            label-text-align="center"
          >
            <el-upload
              class="avatar-uploader"
              action="123"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :on-change="onchange"
              :before-upload="beforeAvatarUpload"
            >
              <img v-if="imageUrl" :src="imageUrl" class="avatar" style="width:100px;height:100px;" />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button size="small" type="primary" @click="Insert('form2')">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>
<script>
import axios from '@/http/axios'
export default {
  data() {
    return {
      options: [
        {
          value: '手机',
          label: '手机'
        },
        {
          value: '平板.笔记本',
          label: '平板.笔记本'
        },
        {
          value: '电视',
          label: '电视'
        },
        {
          value: '路由器',
          label: '路由器'
        },
        {
          value: '耳机',
          label: '耳机'
        }
      ],
      susuo: '',
      total: 0,
      page: 1,
      loading: false,
      tableData: [],
      imageUrl: '',

      formLabelWidth: '100px',
      dialogFormVisible: false,
      dialogFormVisible2: false,

      form: {},
      form2: {}
    }
  },
  created() {
    this.findAll()
  },
  methods: {
    findAll() {
      this.loading = true
      axios
        .get('/goods/Good_list/?page=' + this.page + '&page_size=' + 10)
        .then(result => {
          this.loading = false
          console.log(result)
          this.total = result.data.count
          console.log(this.total)
          this.tableData = result.data.results
        })
    },
    closeFormDialog() {
      this.dialogFormVisible = false
      if (this.$refs['form'] != undefined) {
        this.$refs['form'].resetFields()
      }
      this.form = {}
      this.findAll()
    },
    closeForm2Dialog() {
      this.dialogFormVisible2 = false
      if (this.$refs['form2'] != undefined) {
        this.$refs['form2'].resetFields()
      }
      this.findAll()
    },
    AddUser(form) {
      // 新增用户
      console.log(this.blobb)
      // this.$refs[form].clearValidate();
      this.dialogFormVisible = false
      var formData = new FormData()
      formData.append('good_name', this.form.good_name)
      formData.append('good_price', this.form.good_price)
      formData.append('good_brand', this.form.good_brand)
      formData.append('good_content', this.form.good_content)
      formData.append('good_parameter', this.form.good_parameter)
      formData.append('good_type', this.form.good_type)
      formData.append('good_num', this.form.good_num)
      formData.append('good_img', this.blobb, 'userimg.jpg')
      console.log(this.form)
      var options = {
        url: '/goods/Good_Create/',
        data: formData,
        method: 'post',
        contentType: false,
        headers: { 'Content-Type': 'multipart/form-data' }
      }
      axios(options)
        .then(result => {
          this.$notify.success({
            title: '成功',
            message: '添加商品成功'
          })
          this.findAll()
          this.$refs[form].clearValidate()
        })
        .catch(error => {
          this.$notify.error({
            title: '网络链接错误',
            message: '加载数据失败'
          })
        })
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
    },
    handleCurrentChange2(val) {
      this.page = val
      console.log(this.page)
      this.findAll()
    },
    handleCurrentChange(val) {
      // 表格
      this.currentRow = val
    },
    search() {
      this.type = '查询到的所有结果'
      axios
        .get(
          '/goods/Good_list/?page=' +
            this.page +
            '&page_size=' +
            30 +
            '&search=' +
            this.susuo
        )
        .then(result => {
          console.log(result)
          this.total = result.data.count
          console.log(this.total)
          this.tableData = result.data.results
        })
    },
    addbtndialog() {
      // 新增按钮
      this.form = { good_price: 9999, good_num: 9999 }
      this.dialogFormVisible = true
      this.imageUrl = null
    },
    ExitMaterial(row) {
      // 修改按钮
      this.form2 = row
      this.blobb = ''
      this.imageUrl = this.form2.good_img
      this.dialogFormVisible2 = true
    },
    Insert(form2) {
      // 修改
      this.dialogFormVisible2 = false
      var formData = new FormData()
      formData.append('id', this.form2.id)
      formData.append('good_name', this.form2.good_name)
      formData.append('good_price', this.form2.good_price)
      formData.append('good_brand', this.form2.good_brand)
      formData.append('good_content', this.form2.good_content)
      formData.append('good_parameter', this.form2.good_parameter)
      formData.append('good_type', this.form2.good_type)
      formData.append('good_num', this.form2.good_num)
      if (this.blobb != '') {
        formData.append('good_img', this.blobb, 'userimg.jpg')
      }

      var options = {
        url: '/goods/Good_Update/',
        data: formData,
        method: 'post',
        contentType: false,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios(options)
        .then(result => {
          this.$notify.success({
            title: '成功',
            message: '修改商品信息成功'
          })
          this.findAll()
          this.$refs[form2].clearValidate()
        })
        .catch(error => {
          this.findAll()
          this.$notify.error({
            title: '网络链接错误',
            message: '加载数据失败'
          })
        })
    }
    // DeleteMaterial(row) {
    //   // 删除按钮
    //   this.$confirm("此操作将永久删除商品, 是否继续?", "提示", {
    //     confirmButtonText: "确定",
    //     cancelButtonText: "取消",
    //     type: "warning"
    //   }).then(() => {
    //     axios
    //       .post("/goods/Good_Delete/", { 'good_id': row.id })
    //       .then(result => {
    //         this.$notify.success({
    //           title: "成功",
    //           message: "删除商品成功"
    //         });
    //         this.findAll();
    //       })
    //       .catch(error => {
    //         this.findAll();
    //         this.$notify.error({
    //           title: "网络链接错误",
    //           message: "加载数据失败"
    //         });
    //       });
    //   });
    // },
  }
}
</script>



