#encoding=gbk
__author__ = 'wangchao'
'''
索引某个目录中的所有文件，进行文件字符操作
'''

import os
import re

cou_file=0
cou_ice=0
list_ice = []

def main():
    p = 'D:/work/code_now/yum/103svn_yumphone1_0/src'
    loopDir(p)
    print 'cou_file:'+str(cou_file)
    print 'cou_ice:'+str(cou_ice)
    print len(list_ice)
    print len( list(set(list_ice)) )
    for i in list(set(list_ice)):
        print "'"+i+"',"

def loopDir(path):
    global cou_file
    s = os.sep
    for i in os.listdir(path):
        file_path = path+s+i
        file_path = file_path.replace('\\',s)
        if os.path.isfile(file_path):
            cou_file=cou_file+1
            # print 'file:'+file_path
            operFile(file_path)
        if os.path.isdir(file_path):
            loopDir(file_path)


def operFile(path):
    global cou_ice
    file_my = open(path)
    for l in file_my:
        if l.find('"swap_type"')>-1:
            cou_ice = cou_ice+1
            
            # l = re.sub(',.*','',l.replace('{','').replace('}','').replace('"swap_type",','')).replace('"','')
            # print l.strip()
            
            l = re.sub('.*"swap_type"','',l)
            l = re.sub('},.*','',l).replace(',','').replace('"','').strip()
            list_ice.append(l)
    file_my.close()

    
if __name__=='__main__':
    main()
    # operFile()
    print 'end'
