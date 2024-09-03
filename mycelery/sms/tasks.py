import time,logging

from mycelery.main import app

log = logging.getLogger("django_celery")

@app.task
def send_sms(mobile):
    print("{}开始发送短信".format(mobile))
    time.sleep(5)
    return "{}短信发送完成".format(mobile)