/**
 * Created by wangchao on 2015/3/29.
 */
var fs = require('fs');
var dateFormat = require('dateformat');


createDirName('sssss');

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
