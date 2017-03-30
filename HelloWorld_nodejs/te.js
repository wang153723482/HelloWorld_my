/**
 * Created by wangchao on 2015/3/10.
 */
var express = require('express');

var app = express();

app.get('/',function(req,res){
    res.send('this is test');
});

app.listen('3002');