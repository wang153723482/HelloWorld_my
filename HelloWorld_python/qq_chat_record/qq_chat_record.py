# coding: UTF-8

import time


def is_valid_date(s):
    try:
        time.strptime(s, '%Y-%m-%d %H:%M:%S')
        return True
    except:
        return False


def main():
    file = open('data.txt')
    d = dict()
    for line in file:
        if '' == line:
            continue
        elif is_valid_date(line[0:19]):
            _user = line[20:].replace('【冒泡】', '').replace('【活跃】', '').replace('【吐槽】', '').replace(' ', '').replace('?',
                                                                                                                   '')
            if _user in d:
                d[_user] += 1
            else:
                d[_user] = 1

    d = sorted(d.items(), key=lambda e: e[1], reverse=True)

   

    result_file = open('result_file.txt', 'a')
    print d 
    for dd in d:
        result_file.write(str(dd[1])+' '+dd[0])
    result_file.close()


if __name__ == '__main__':
    main()
