package com.wangc.p04_adapter.test1;

/**
 * Created by wangchao on 2017/2/27.
 */
public class Main {
    public static void main(String[] args){
        //原来的导出功能，Export是一个接口，ExportDb是利用数据库导出的实现类
        
        Export export = new ExportDb();//new一个实现类或者注入
        export.exc();//导出
        
        
        //现在有了一个新的导出功能，没有实现Export接口。
        Export exportNew = new ExportAdapter();//new一个适配器的实例或者注入
        exportNew.exc();//导出
        
        
    }    
}
