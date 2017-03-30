/**
 * Created by wangchao on 2015/3/29.
 */

var readOF=require("readof");

var pic = 'http://i4.bbs.fd.zol-img.com.cn/t_s1200x5000/g4/M04/06/0A/Cg-4y1TO0h2IfG6YAAvaerz2olMAATpMAFqu2MAC9qS364.jpg';

readOF.read(pic,'img/my.jpg',function(data,error){
    if(!error){
        console.log('asd');
    }
});