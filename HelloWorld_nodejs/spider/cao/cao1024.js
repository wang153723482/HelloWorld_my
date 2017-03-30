/**
 * Created by wangchao on 2016/2/2.
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


var url = 'http://t66y.com/thread0806.php?fid=20&search=&page=';


for(var i=3; i<32; i++){
    readPage(url+i);    
}





function readPage(url){
    var urls = [];
    var base_url = 'http://t66y.com/';

    request(url, function (err, res, body) {
        if (!err && res.statusCode == 200) {
            var html = iconv.decode(body, 'gbk');
            //console.log(html);
            var $ = cheerio.load(html, {decodeEntities: false});
            var tableContent = $('#ajaxtable');
            //console.log(tableContent.html());

            tableContent.find('tbody tr td h3 a').each(function(){
                var detail_page = $(this).attr('href');
                console.log( detail_page );

                request(base_url+detail_page, function (err,res,body) { //打开下载页
                    if (!err && res.statusCode == 200) {
                        var html_down_load_page = iconv.decode(body,'gbk');
                        //console.log(html_down_load_page);
                        var $ = cheerio.load(html_down_load_page, {decodeEntities: false});

                        var title = $('#main div table tr td b').html().replace(/<a.*<\/a>/,'').replace('&raquo;','').replace(' ','');
                        console.log(title);

                        var content_words = $('.tpc_content');
                        for(var i=0; i<content_words.length; i++){
                            //console.log( $(content_words[i]).html() );
                            writeFile('txt/'+title+'.txt',$(content_words[i]).html().replace(/<br>/g,'\r\n').replace(/&nbsp;/g,'') );
                        }
                    }else{
                        console.log(res.statusCode);
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

function writeFile(file,str){
    // 测试用的中文  
    //var str = "我是一个人Hello myself!";
    // 把中文转换成字节数组  
    var arr = iconv.encode(str, 'gbk'); // 当前文件编码为utf8才有效，不知道为什么

    // appendFile，如果文件不存在，会自动创建新文件  
    // 如果用writeFile，那么会删除旧文件，直接写新文件  
    fs.appendFile(file, arr, function(err){
        if(err)
            console.log("fail " + err);
        else
            console.log("写入文件ok");
    });
}  
