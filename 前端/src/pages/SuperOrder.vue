<template>
  <div class="SuperOrder">
    <br />
    <h1 style="margin-left:20px;">订单管理</h1>
    <div style="margin-top: 10px;">
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
        <el-table-column
          label="订单号"
          prop="order_num"
          type="index"
          header-align="center"
          align="center"
          width="200px"
        >
          <template slot-scope="scope">{{scope.row.order_num}}</template>
        </el-table-column>
        <el-table-column prop="user_name" label="用户名" header-align="center" align="center"></el-table-column>
        <el-table-column
          prop="order_time"
          label="下单时间"
          header-align="center"
          align="center"
          width="150px"
        >
          <template slot-scope="scope">{{formatDate(scope.row.order_time)}}</template>
        </el-table-column>

        <el-table-column prop="order_aceptman" label="收货人姓名" header-align="center" align="center"></el-table-column>
        <el-table-column
          prop="order_address"
          label="收货人地址"
          header-align="center"
          align="center"
          width="150px"
        ></el-table-column>
        <el-table-column prop="order_phone" label="收货人电话" header-align="center" align="center"></el-table-column>
        <el-table-column prop="max_price" label="订单总额" header-align="center" align="center">
          <template slot-scope="scope">{{scope.row.max_price}} 元</template>
        </el-table-column>
        <el-table-column prop="order_status" label="订单确认情况" header-align="center" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.order_status">已确认订单</span>
            <span v-else>未确认订单</span>
          </template>
        </el-table-column>

        <el-table-column
          prop="Operation"
          label="操作"
          width="150px"
          header-align="center"
          align="center"
        >
          <template slot-scope="scope">
            <el-button
              v-if="! scope.row.order_status"
              type="success"
              title="确认订单"
              icon="el-icon-sold-out"
              style="width: 30px;height: 30px;padding: 0px"
              @click="queren(scope.row)"
            ></el-button>
            <el-button
              type="info"
              title="查看订单详情"
              icon="el-icon-tickets"
              style="width: 30px;height: 30px;padding: 0px"
              @click="ExitMaterial(scope.row)"
            ></el-button>
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
    <!-- --------------------模态框 -->
    <el-dialog title="订单详情" :visible.sync="dialogVisible" width="80%" :before-close="handleClose">
      <div>
        <div>
          <div
            style="background-color: rgba(176,176,176,0.2);border-left: 5px solid #ff6700;font-size:12px;height:50px;line-height:25px;color:#00000;font-weight: bold;"
          >
            &emsp;&emsp;&emsp;订单时间: {{formatDate(this.formdata.order_time)}} &emsp;订单号: {{this.formdata.order_time+this.formdata.order_num}} &emsp;&emsp;&emsp;总价： {{this.formdata.max_price}}元 &emsp;&emsp;&emsp;
            <br />
            &emsp;&emsp;&emsp;收货人： {{this.formdata.order_aceptman}} &emsp;&emsp;&emsp; 收获地址： {{this.formdata.order_address}} &emsp;&emsp;&emsp; 联系方式： {{this.formdata.order_phone}} &emsp;&emsp;&emsp;
            <span
              v-if="this.formdata.order_status"
            >已确认订单</span>
            <span v-else>未确认订单</span>

            <br />
          </div>
          <el-table
            ref="multipleTable"
            :data="this.formdata.data"
            tooltip-effect="dark"
            style="width: 90%;margin-left:5%;"
          >
            <el-table-column prop="good_img" label="商品图片">
              <template slot-scope="scope">
                <img :src="base+'media/'+scope.row.good_img" alt width="50px;" height="50px;" />
              </template>
            </el-table-column>

            <el-table-column prop="good_name" label="商品名称"></el-table-column>
            <el-table-column prop="good_price" label="单价"></el-table-column>
            <el-table-column prop="good_num" label="数量" show-overflow-tooltip></el-table-column>
            <el-table-column label="小计" show-overflow-tooltip>
              <template slot-scope="scope">{{scope.row.good_num * scope.row.good_price}}</template>
            </el-table-column>
          </el-table>
          <div class="clear"></div>
        </div>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="queding()">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import axios from '@/http/axios'
export default {
  data() {
    return {
      total: 0,
      page: 1,
      loading: false,
      tableData: [],
      formLabelWidth: '100px',
      dialogVisible: false,
      formdata: {},
      base: axios.defaults.baseURL
    }
  },
  created() {
    this.findAll()
  },
  methods: {
    findAll() {
      this.loading = true
      axios
        .get('/goods/Order_List/?page=' + this.page + '&page_size=' + 10)
        .then(result => {
          this.loading = false
          console.log(result)
          this.total = result.data.count
          console.log(this.total)
          this.tableData = result.data.result
        })
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
    formatDate(now) {
      var Now = new Date(now)
      var year = Now.getFullYear()
      var month = Now.getMonth() + 1
      var date = Now.getDate()
      var hour = Now.getHours()
      var minute = Now.getMinutes()
      var second = Now.getSeconds()
      return (
        year +
        '-' +
        month +
        '-' +
        date +
        ' ' +
        hour +
        ':' +
        minute +
        ':' +
        second
      )
    },
    queren(row) {
      console.log(row.order_num)
      axios
        .post('/goods/Order_Update/', {
          order_num: row.order_num,
          order_status: 1
        })
        .then(result => {
          this.findAll()
          this.$notify.success({
            title: '确认订单成功',
            message: '确认订单成功'
          })
        })
        .catch(error => {
          this.$notify.error({
            title: '确认订单成功',
            message: '确认订单成功'
          })
        })
    },
    handleClose() {
      this.dialogVisible = false
      if (this.$refs['form'] != undefined) {
        this.$refs['form'].resetFields()
      }
    },
    ExitMaterial(row) {
      console.log(row)
      this.formdata = row
      console.log(this.formdata)
      this.dialogVisible = true
    },
    queding() {
      this.dialogVisible = false
    }
  }
}
</script>



