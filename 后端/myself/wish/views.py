from rest_framework.views import APIView
from alipay import AliPay
from rest_framework.response import Response

class alipayView(APIView):

    def post(self, request):
        alipay = AliPay(
            appid="2016092900622837",
            app_notify_url=None,  # 默认回调url
            app_private_key_path="./wish/private_key.txt",
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_path="./wish/alipay_public_key.txt",
            sign_type="RSA", # RSA 或者 RSA2
        debug = False,  # 默认False
        )
        subject = "ThinkPad X1"
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no="20161119",
            total_amount=0.1,
            subject=subject,
            return_url="https://www.baidu.com",
            notify_url=""  # 可选, 不填则使用默认notify url
        )

        return Response(data={"code": 200, "url": "https://openapi.alipaydev.com/gateway.do?" + order_string})


