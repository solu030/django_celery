from django.shortcuts import HttpResponse
from datetime import datetime, timedelta
from mycelery.sms.tasks import send_sms
from mycelery.pay.tasks import start_pay
# Create your views here.
def index(request):
    #异步请求
    send_sms.delay("1111546545")
    start_pay.delay("1234")
    return HttpResponse("OK")
    #定时发送
    # ctime = datetime.now()
    # utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    # task_time = utc_ctime + timedelta(seconds=10)
    # result = send_sms.apply_async(["1444444"],eta=task_time)
    # return HttpResponse(result.id)