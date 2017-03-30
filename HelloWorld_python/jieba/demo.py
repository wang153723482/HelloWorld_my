# encoding=utf-8
__author__ = 'wangchao'
#python2 pip install jieba
#python3 pip3 install jieba3k

import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode:", "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode:", "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))


print '=============='
seg_list = jieba.cut_for_search("6号线 房主诚心招三居合租 宜家风格 拎包入住 配备齐全")  # 搜索引擎模式
aa= ", ".join(seg_list)
print(aa)