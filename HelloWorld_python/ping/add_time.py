# encoding=utf8

import datetime

f = open('ping.201701061025.log', 'r')
f_new = open('ping.new.log', 'w')
t_time = '2017-01-06 10:25:00'
t = datetime.datetime.strptime(t_time, '%Y-%m-%d %H:%M:%S')

num_max = 0

i = 0
seq = ''
_min = 9999999999.9
_avg = 0.0
_max = 0.0
_sum = 0.0

pre_seq = ''

for l in f:
    i += 1
    if i == 1:
        continue
    seq = l.split(' ')[4].replace('icmp_seq=', '')
    if not '' == pre_seq and not int(seq) - int(pre_seq) == 1:
        for i in range(int(seq) - int(pre_seq) - 1):
            seconds = int(seq) + num_max * 65536 + 1
            t_new = t + datetime.timedelta(seconds=seconds)  # 增加seconds秒 
            a = '1008 bytes from 10.6.17.50: icmp_seq=' + str(int(seq) + i + 1) + ' ttl=55 time=6.44 ms t=' + str(t_new)+ '\n'
            f_new.write(line_new)
        pass

    _time = float(l.split(' ')[6].replace('time=', '').replace(' ms', ''))
    if _time < _min:
        _min = _time

    if _time > _max:
        _max = _time

    _sum += _time

    seconds = int(seq) + num_max * 65536 + 1
    if '65535' == seq:
        num_max += 1
    t_new = t + datetime.timedelta(seconds=seconds)  # 增加seconds秒 
    line_new = l.replace('\n', '') + ' t=' + str(t_new) + '\n'
    f_new.write(line_new)
    pre_seq = seq  # 这次的seq保存到per_seq中，下一次循环使用

total_seq = 65535 * num_max + int(seq)
loss = total_seq - i
print(str(total_seq) + ' packets transmitted,' + str(i) + ' received,' + str(
    round(1.0 * loss / total_seq * 100, 2)) + '% loss')
print('min/avg/max = ' + str(_min) + '/' + str(round(_sum / i, 2)) + '/' + str(_max) + ' ms')


# 2 packets transmitted, 2 received, 0% packet loss, time 1291ms
# rtt min/avg/max/mdev = 0.172/0.741/1.310/0.569 ms
