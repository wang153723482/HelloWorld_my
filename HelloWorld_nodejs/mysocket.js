/**
 * Created by wangchao on 2015/3/7.
 */

var express = require('express');

var app = express();

app.use(express.static(__dirname));

var server = require('http').createServer(app);

var io = require('socket.io')(server);

io.on('connection',function(socket){
    console.log('connection--this is socket.io server');

    socket.on('message',function(data){
        console.log(data);

    });

});

server.listen(8080);