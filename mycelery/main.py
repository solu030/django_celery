import os
from celery import Celery

app = Celery('mycelery')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app.config_from_object('mycelery.config')

app.autodiscover_tasks(['mycelery.sms', 'mycelery.pay'])

# 启动celery命令
# celery -A mycelery.main worker -l info -P eventlet