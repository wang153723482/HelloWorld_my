# encoding=utf8
from locust import task, HttpUser, constant
from locust.contrib.fasthttp import FastHttpUser
from locust.exception import RescheduleTask
import os
import json
import threading
import queue


class MyUser(HttpUser):
    host = 'http://10.6.21.86:43996'
    url = '/starbucksCommQuery/MSCode'
    q = queue.Queue()
    with open('data.csv') as f:
        for i in f.readlines():
            q.put(i)

    def on_start(self):
        pass

    wait_time = constant(1)

    @task
    def query(self):

        data = self.q.get()
        headers = {'Content-Type': 'application/json'}
        with self.client.post(self.url, headers=headers, data=data) as resp:
            if 200 != resp.status_code:
                # raise RescheduleTask()
                pass
        # 用完以后把数据再次放到队列中，达到重复使用的效果
        self.q.put(data)


if __name__ == '__main__':
    os.system('locust -f quick_2_test.py --headless -u2 -r2 -t1')
