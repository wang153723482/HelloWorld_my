# coding: UTF-8

import time


def is_valid_date(s):
    try:
        time.strptime(s, '%Y-%m-%d %H:%M:%S')
        return True
    except:
        return False


# 处理空行，剩下的内容写入list。
# 处理连续信息，保持固定格式：第一行：时间，第二行：用户，第三行：信息；第四行：时间，第5行：用户，第6行：信息。。。
# 每三行处理为一个对象，插入表或者list

def main():
    file = open('data.txt')
    l = list()
    for line in file:
        
        if ''==line or '\n'==line:
            continue
        else:
            l.append(line.strip('\n'))

    
    l2 = list()
    tmp_msg = ''
    for ll in l:
        ll = ll.strip()
        print ll
        print ll[0:19]
        if is_valid_date(ll[0:19]):
            l2.append(ll[0:19])
            l2.append(ll[19:]) #从第19个字符开始截取到最末一位
            tmp_msg = ''
        else:
            tmp_msg+=ll
            l2.append(tmp_msg)
        print l2
    
    print l2
    
    if True:
        return
        
        # if '' == line:
        #     continue
        # elif is_valid_date(line[0:19]):
        #     _user = line[20:].replace('【冒泡】', '').replace('【活跃】', '').replace('【吐槽】', '').replace(' ', '').replace('?',
        #                                                                                                            '')
        #     
        #     if _user in d:
        #         d[_user] += 1
        #     else:
        #         d[_user] = 1

    # d = sorted(d.items(), key=lambda e: e[1], reverse=True)

   

    # result_file = open('result_file.txt', 'a')
    # print d 
    # for dd in d:
    #     result_file.write(str(dd[1])+' '+dd[0])
    # result_file.close()
    # 

if __name__ == '__main__':
    main()
