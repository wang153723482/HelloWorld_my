/**
 * Created by wangchao on 2016/1/29.
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


var url = 'http://www.pixvol.com/book/10250.htm';
downPic(url);
//
//var a = 'http://file2.pixvol.com/7bf52dab1454332478/0001/10250/10250-1045-%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97-%E7%AC%AC45%E5%8D%B7.mobi';
//saveFile(a,'D:/work_nodejs/mynode/spider/aa.mobi');


function downPic(url){
    var urls = [];
    var path = 'D:/work_nodejs/mynode/spider/kenan/';

    request(url, function (err, res, body) {
        if (!err && res.statusCode == 200) {
            var html = iconv.decode(body, 'utf-8');
            //console.log(html);
            var $ = cheerio.load(html, {decodeEntities: false});
            var tableContent = $('#div_mobi');
            //console.log(tableContent.html());

            tableContent.find('tr td a').each(function(){
                var url_download_page = $(this).attr('href');
                //console.log( url_download_page );

                request(url_download_page, function (err,res,body) { //打开下载页
                    if (!err && res.statusCode == 200) {
                        var html_down_load_page = iconv.decode(body,'utf-8');
                        //console.log(html_down_load_page);
                        var $ = cheerio.load(html_down_load_page, {decodeEntities: false});
                        var _this = $('#vol_downimg').find('a')[0];
                        var url_down = $(_this).attr('href');
                        var file_name = $(_this).html().replace(/10250-[0-9]{4}-/,'');
                        console.log(url_down);
                        saveFile(url_down,path+file_name);
                        console.log(file_name+' is over.');
                    }
                });
            });

            
            

        }else{
            console.log('open the url is error');
        }
    });
    
    console.log(111111111);
    console.log(urls);
}


function saveFile(fileUrl,path){
    readOF.read(fileUrl,path,function(data,error){
        if(!error){
            console.log('写文件失败('+url+')');
        }else{

        }
    });
    
}
