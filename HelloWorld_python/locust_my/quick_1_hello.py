# encoding=utf8
from locust import task
from locust.contrib.fasthttp import FastHttpUser
import os


# locust 1.4.1
class MyUser(FastHttpUser):
    host = 'http://127.0.0.1:8080'  # 指定被测目标的域名或ip，这里指定了执行的时候就不用-host指定了

    @task  # 使用@task注解声明一个任务
    def index(self):
        response = self.client.get('/hello')  # 使用self的属性指定http请求，可以是get或post或其他的method


if __name__ == '__main__':
    os.system('locust -f quick_1_hello.py --headless -u1 -r1 -t1')  # -u指定了虚拟用户数量，-r指定了启动虚拟用户的频率，-t指定了执行事件
