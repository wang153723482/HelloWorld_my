package com.wangc.p04_adapter;

/**
 * @author: wangchao
 * Date: 2016/3/5 16:04
 * Description:适配器
 * Target 是客户端目前一直在使用的接口
 */
public class Adapter implements Target{
    
    //new一个或者注入一个
    Adaptee adaptee = new Adaptee(); //被适配的类，原来就有的类。

    @Override
    public void say() {
        adaptee.sayHello();
    }
}
