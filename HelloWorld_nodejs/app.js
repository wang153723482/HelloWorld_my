/**
 * Created by wangchao on 2015/3/7.
 */

var express = require('express');
var url = require('url');
var bodyParse = require('body-parser');
var multer = require('multer');
var util = require('util');
var fs = require('fs');

var app = express();

app.use(bodyParse.json());
app.use(bodyParse.urlencoded({extended:true}));
app.use(multer({dest:'./'}));

app.get('/',function(req,res){
    res.sendfile('./index.html');
});

app.use('/money',function(req,res,next){
    res.money = 100;
    next();
});

app.use('/money',function(req,res,next){
    res.money = res.money-30;
    res.send(res.money+'');
});

app.post('/reg',function(req,res,next){
    var urlObj = url.parse(req.url,true);
    res.end( JSON.stringify( urlObj.query ) );

});

app.listen(3001);