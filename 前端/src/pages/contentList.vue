<template>
  <div class="contentList">
    <!-- 列表详情页面 -->
    <!-- start danpin -->
    <div class="danpin center">
      <el-input
        v-model="susuo"
        placeholder="请输入内容"
        style="width:300px;margin-left:1000px;margin-top:30px"
        @change="search"
      ></el-input>
      <div class="biaoti center">{{this.type?this.type:'所有商品'}}</div>
      <div class="main center">
        <div
          class="mingxing fl mb20"
          @click="contentlink(item.id)"
          :key="item"
          v-for="item in goodslist"
          style="margin:5px;border:2px solid #fff;width:230px;cursor:pointer;"
          onmouseout="this.style.border='2px solid #fff'"
          onmousemove="this.style.border='2px solid red'"
        >
          <div class="sub_mingxing">
            <a>
              <img :src="item.good_img" alt />
            </a>
          </div>
          <div class="pinpai">{{item.good_name}}</div>
          <div class="youhui">{{item.good_parameter}}</div>
          <div class="jiage">{{item.good_price}}元</div>
        </div>
        <div class="clear"></div>
        <div class="page" style="height:50px">
          <el-pagination
            background
            prev-text="上一页"
            @current-change="handleCurrentChange2"
            next-text="下一页"
            layout="prev, pager, next"
            :total="total"
            :page-size="30"
            style="margin-top: 25px;float: right;margin-right: 15px;"
          ></el-pagination>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from '@/http/axios'
export default {
  data() {
    return {
      type: '',
      susuo: '',
      goodslist: [],
      total: 6,
      page: 1
    }
  },
  created() {
    this.findAll()
  },
  methods: {
    findAll() {
      this.susuo = ''
      this.type = this.$route.query.id
      console.log(this.type)
      axios
        .get(
          '/goods/Good_list/?page=' +
            this.page +
            '&page_size=' +
            30 +
            '&search=' +
            this.type
        )
        .then(result => {
          console.log(result)
          this.total = result.data.count
          console.log(this.total)
          this.goodslist = result.data.results
        })
    },
    contentlink(id) {
      this.$router.push({ path: '/content', query: { id: id } })
    },
    handleCurrentChange2(val) {
      this.page = val
      console.log(this.page)
      this.findAll()
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
          this.goodslist = result.data.results
        })
    }
  }
}
</script>


