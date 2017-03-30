/*
* download picture of the zol.com.cn.
*
* */

var originRequest = require('request');
var cheerio = require('cheerio');
var iconv = require('iconv-lite');
var headers = {
    'User-Agent': 'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'
};
var fs = require('fs');
var rOption = {
    flags : 'r',
    encoding : null,
    mode : 0666
};  
var wOption = {
    flags: 'a',
    encoding: null,
    mode: 0666
};
var readOF=require("readof");
var dateFormat = require('dateformat');

function request (url, callback) {
    var options = {
        url: url,
        encoding: null,
        headers: headers
    };
    originRequest(options, callback)
}

//每月《人像版优秀作品》
var url = 'http://bbs.zol.com.cn/dcbbs/d16_82074.html'; //2
url = 'http://bbs.zol.com.cn/dcbbs/d16_79900.html';//1
url = 'http://bbs.zol.com.cn/dcbbs/d16_71769.html';//12
url = 'http://bbs.zol.com.cn/dcbbs/d16_62214.html';//11
url = 'http://bbs.zol.com.cn/dcbbs/d16_67814.html';//10
url = 'http://bbs.zol.com.cn/dcbbs/d16_52392.html';//9
url = 'http://bbs.zol.com.cn/dcbbs/d16_4745.html';//8
url = '';//7
url = 'http://bbs.zol.com.cn/dcbbs/d16_7091.html';//6
url = 'http://bbs.zol.com.cn/dcbbs/d16_8329.html';//5
url = '';//4
url = 'http://bbs.zol.com.cn/dcbbs/d16_10936.html';//3     NG
url = 'http://bbs.zol.com.cn/dcbbs/d16_12017.html';//2    NG
url = 'http://bbs.zol.com.cn/dcbbs/d16_12937.html';//1     NG

//2013
 url = 'http://bbs.zol.com.cn/dcbbs/d16_13642.html';//12
 url = 'http://bbs.zol.com.cn/dcbbs/d16_14358.html';//11
 url = 'http://bbs.zol.com.cn/dcbbs/d16_18209.html';//10
 url = 'http://bbs.zol.com.cn/dcbbs/d16_26808.html';//9
 url = 'http://bbs.zol.com.cn/dcbbs/d16_14350.html';//8
 url = 'http://bbs.zol.com.cn/dcbbs/d16_15981.html';//7    NG

 //2011
/* url = '';//8
 url = '';//8
 url = '';//8
 url = '';//8

 */


request(url, function (err, res, body) {
    if (!err && res.statusCode == 200) {
        var html = iconv.decode(body, 'gb2312');
        //console.log(html);
        var $ = cheerio.load(html, {decodeEntities: false});
        var bookContent = $('#bookContent');
        //console.log(bookContent.html());

        bookContent.find('a').each(function(){
            var reg = /^http.*/;
            var this_v = $(this).html();
            if( reg.test( this_v ) ){
                console.log(this_v);
                downPic(this_v);
            }

        });
    }else{
        console.log('open the url is error');
    }

});

/*创建目录
* dirname为空，创建时分秒的目录*/
function downPic(url){

    request(url, function (err, res, body){
        if (!err && res.statusCode == 200) {
            var html = iconv.decode(body, 'gb2312');
            //console.log(html);
            var $ = cheerio.load(html, {decodeEntities: false});
            var bookContent = $('#bookContent');
            if( null==bookContent ){
                console.log("===================haha====")
            }
            var bookTitle = "";
            try{
                bookTitle = $("#bookTitle h1").html().replace(/<.*/,'').replace('/','');
            }catch (err){

            }

            //console.log(bookTitle );
            var dirName = createDirName(bookTitle);
            //console.log( "============"+dirName );

            var n = 0;

            bookContent.find('img').each(function(){
                n = n + 1;
                var fileName = '_'+n+'.jpg';
                var this_v = $(this).attr('src');
                //console.log( this_v );
                readOF.read(this_v,dirName+'/'+fileName,function(data,error){
                    console.log(dirName+'/'+fileName);
                    if(!error){
                        console.log('写文件失败('+url+','+dirName+'/'+fileName+')');
                    }else{

                    }
                });

            });

        }else{
            console.log('open the url is error');
        }
    });

}


//创建目录，如果报错则创建一个当前  yymmddhhmmss 的目录
function createDirName(dirName){
    if( null==dirName || ''==dirName ){
        var now = new Date();
        dirName = dateFormat(now, "yyyymmddHHMMss");
    }

    dirName = 'img/'+dirName;
    var folder_exists = fs.existsSync(dirName);
    if( !folder_exists ){
        try{
            fs.mkdir(dirName);
        }catch(err){
            fs.mkdir(thisDate);
            return thisDate;
        }

    }
    return dirName;

    //这里应该增加异常处理，如果创建报错，可能是dirName包含特殊字符，在catch理创建 thisDate 的目录

}


//downPic('http://bbs.zol.com.cn/dcbbs/d16_81836.html','');