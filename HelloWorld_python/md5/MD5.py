#python2.*
__author__ = 'wangchao'

import hashlib


def main():
    print 1
    print MD5encrypt('10000Rb498d0f8bfab48b7a2abdf25ee51c5a51480402506335{"MsgInfo":{"CommType":"REQ","TxnType":"ActivateCertificate","TxnVersion":"0.0.1","Charset":"UTF-8"},"ChannelInfo":{"ChannelLang":"zh_CN","ChannelHostIP":"10.100.70.100","ChannelRefNo":"Rb498d0f8bfab48b7a2abdf25ee51c5a51480402506335","ChannelTimeStamp":"1477466428035","ChannelTimeZone":"CCT","SAFFlag":"","SAFTimeStamp":""},"RetailerInfo":{"StoreID":"20160427","StoreName":"zihexintest","StoreTimeZone":"CCT","TerminalID":"110","TerminalRefNo":"101152027452","TerminalTimeStamp":"1477451436297","TerminalLang":"zh_CN","MerchantId":"1001","MerchantName":"TEST2","MerchantDivId":"1001126"},"ServiceData":{"CardList":[{"CardNo":"8886660127000888888","InputType":"02","TrackI":"","TrackII":"","TrackIII":"","FaceValue":"10000","CNYCode":"CHN"}]}}*&(%$#@WS@!S')


def MD5encrypt(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()



if __name__=='__main__':
    main()