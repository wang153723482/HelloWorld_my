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

var page_url = 'http://pp.163.com/pp/#p=11&c=-1&m=3&page=1';
readPage(page_url);


function readPage(url){
    request(url, function (err, res, body) {
        if (!err && res.statusCode == 200) {
            var html = iconv.decode(body, 'gb2312');
            console.log(html);
            var $ = cheerio.load(html, {decodeEntities: false});
            var bookContent = $('#photo_show_main');
            //console.log( bookContent.html() );

        }
    });


}
