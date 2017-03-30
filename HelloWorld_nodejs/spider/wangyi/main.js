/**
 * Created by wangchao on 2015/4/13.
 * 只能下载单独网页上的图片
 */
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


var urls = [
    'http://pp.163.com/chenjiasso/pp/17890060.html',
'http://pp.163.com/heimu888888/pp/17891022.html',
    'http://pp.163.com/heinuo/pp/17909033.html',
        'http://pp.163.com/mixiaoka/pp/17887037.html',
            'http://pp.163.com/heimu888888/pp/17903007.html',
                'http://pp.163.com/deer-vision/pp/17889035.html',
                    'http://pp.163.com/changshamike/pp/17891015.html',
                        'http://pp.163.com/liwan/pp/17909056.html',
                            'http://pp.163.com/xiaott500/pp/17886013.html'
];


for( var i=0;i<urls.length;i++ ){
    downPic(urls[i]);
}


function downPic(url){
    request(url, function (err, res, body) {
        if (!err && res.statusCode == 200) {
            var html = iconv.decode(body, 'gb2312');
            //console.log(html);
            var $ = cheerio.load(html, {decodeEntities: false});
            var bookContent = $('#J-picsContainer');
            //console.log(bookContent.html());
            var p_username_copy = $("#p_username_copy").text().trim();//标题(目录名)
            console.log(p_username_copy);
            fs.mkdir(p_username_copy);

            var gg = $(".g-mainwraper-picsetinfo");
            console.log( gg.html().match() );

            var n = 0;
            bookContent.find('.pic-area img').each(function(){
                n++;
                var this_url = $(this).attr("data-lazyload-src");
                //console.log(this_url);
                readOF.read(this_url,p_username_copy+'/'+n+'.jpg',function(data,error){
                    //console.log(dirName+'/'+fileName);
                    if(!error){
                        console.log('写文件失败('+url+')');
                    }else{

                    }
                });

            });
            console.log(n);
        }else{
            console.log('open the url is error');
        }
    });
}
