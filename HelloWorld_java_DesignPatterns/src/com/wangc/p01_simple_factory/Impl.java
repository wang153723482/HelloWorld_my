package com.wangc.p01_simple_factory;

/**
 * @author: wangchao
 * Date: 2016/1/6 12:01
 * Description:
 */
public class Impl implements Api {
    @Override
    public void sayHello(String name) {
        System.out.println("hello,simple factory.I am "+name);
    }
}
