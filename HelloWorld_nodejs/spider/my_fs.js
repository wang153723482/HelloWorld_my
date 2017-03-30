/**
 * Created by wangchao on 2015/3/29.
 */



var fs = require('fs');
var iconv = require('iconv-lite');

var rOption = {
    flags : 'r',
    encoding : null,
    mode : 0666
}

var wOption = {
    flags: 'a',
    encoding: null,
    mode: 0666
}

/*
 var f = 'http://i4.bbs.fd.zol-img.com.cn/t_s1200x5000/g4/M04/06/0A/Cg-4y1TO0h2IfG6YAAvaerz2olMAATpMAFqu2MAC9qS364.jpg';
 var fileReadStream = fs.createReadStream(f,rOption);
 var fileWriteStream = fs.createWriteStream('./new_myjpg.jpg',wOption);

 fileReadStream.on('data',function(data){
 fileWriteStream.write(data);

 });

 fileReadStream.on('end',function(){
 console.log('readStream end');
 fileWriteStream.end();
 });
 */



var file = "new_my.txt";
var s = '我是一个人Hello myself!';
writeFile(file,s);

function writeFile(file,str){
    // 测试用的中文  
    //var str = "我是一个人Hello myself!";
    // 把中文转换成字节数组  
    var arr = iconv.encode(str, 'gbk'); // 当前文件编码为utf8才有效，不知道为什么
    console.log(arr);

    // appendFile，如果文件不存在，会自动创建新文件  
    // 如果用writeFile，那么会删除旧文件，直接写新文件  
    fs.appendFile(file, arr, function(err){
        if(err)
            console.log("fail " + err);
        else
            console.log("写入文件ok");
    });
}  


