<template>
  <div class="index">
    <!-- 主页页面 -->
    <!-- start banner_x -->
    <div class="banner_x center">
      <a>
        <div class="ad_top fl"></div>
      </a>
      <div class="nav fl">
        <ul>
          <li v-for="type in typeList" :key="type">
            <a @click="contentlistlink(type.name)">{{ type.name }}</a>
          </li>
          <el-input
            v-model="susuo"
            placeholder="请输入内容"
            style="width:300px;margin-left:300px;margin-top:30px"
            @change="search"
            @keyup.enter="search"
          ></el-input>
        </ul>
      </div>
    </div>
    <!-- end banner_x -->
    <!-- start banner_y -->
    <div class="banner_y center">
      <div class="nav">
        <ul>
          <li v-for="type in typeList" :key="type">
            <a @click="contentlistlink(type.name)">{{ type.name }}</a>
            <div class="pop">
              <div class="left fl">
                <div v-for="item in goodslist" :key="item">
                  <div class="xuangou_left fl">
                    <a>
                      <div class="img fl">
                        <img :src="item.good_img" alt width @click="contentlink(item.id)" />
                      </div>
                      <span class="fl" @click="contentlink(item.id)">{{item.good_name}}</span>
                      <div class="clear"></div>
                    </a>
                  </div>
                  <div class="xuangou_right fr" @click="contentlink(item.id)">
                    <a>选购</a>
                  </div>
                  <div class="clear"></div>
                </div>
              </div>
              <div class="ctn fl">
                <div v-for="item in goodslist2" :key="item">
                  <div class="xuangou_left fl">
                    <a>
                      <div class="img fl">
                        <img :src="item.good_img" alt @click="contentlink(item.id)" />
                      </div>
                      <span class="fl" @click="contentlink(item.id)">{{item.good_name}}</span>
                      <div class="clear"></div>
                    </a>
                  </div>
                  <div class="xuangou_right fr" @click="contentlink(item.id)">
                    <a>选购</a>
                  </div>
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
      <div class="main center">
        <div
          class="mingxing fl"
          :key="item"
          v-for="item in goodslist"
          @click="contentlink(item.id)"
        >
          <div class="sub_mingxing">
            <a>
              <img :src="item.good_img" alt />
            </a>
          </div>
          <div class="pinpai">
            <a>{{item.good_name}}</a>
          </div>
          <div class="youhui">{{item.good_content}}</div>
          <div class="jiage">{{item.good_price}}元起</div>
        </div>
        <div class="clear"></div>
      </div>
    </div>
    <div></div>
    <div class="danpin center">
      <div class="biaoti center">耳机</div>
      <div class="main center">
        <div
          class="mingxing fl"
          v-for="item in goodslist8"
          :key="item"
          @click="contentlink(item.id)"
        >
          <div class="sub_mingxing">
            <a>
              <img :src="item.good_img" alt />
            </a>
          </div>
          <div class="pinpai">
            <a>{{item.good_name}}</a>
          </div>
          <div class="youhui">{{item.good_content}}</div>
          <div class="jiage">{{item.good_price}}元起</div>
        </div>
        <div class="clear"></div>
      </div>
    </div>
    <div></div>
    <div class="danpin center">
      <div class="biaoti center">笔记本</div>
      <div class="main center">
        <div
          class="mingxing fl"
          v-for="item in goodslist3"
          :key="item"
          @click="contentlink(item.id)"
        >
          <div class="sub_mingxing">
            <a>
              <img :src="item.good_img" alt />
            </a>
          </div>
          <div class="pinpai">
            <a>{{item.good_name}}</a>
          </div>
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
  data() {
    return {
      susuo: '',
      goodslist: [],
      typeList: [],
    }
  },
  created() {
    this.findall()
  },
  methods: {
    findall() {
      axios.get('/goods/GoodType_List/').then(result=>{
        console.log(result.data.results)
        this.typeList = result.data.results
      })
      axios.get('/goods/Good_list/?page=2&search=音箱').then(result => {
        console.log(result.data.results)
        this.goodslist11 = result.data.results
      })
    },
    search() {
      this.$router.push({ path: '/contentList', query: { id: this.susuo } })
    },
    contentlistlink(name) {
      this.$router.push({ path: '/contentList', query: { id: name } })
    },
    contentlink(id) {
      this.$router.push({ path: '/content', query: { id: id } })
    }
  }
}
</script>

