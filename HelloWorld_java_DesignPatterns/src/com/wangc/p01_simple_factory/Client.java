package com.wangc.p01_simple_factory;

/**
 * @author: wangchao
 * Date: 2016/1/6 12:04
 * Description:
 */
public class Client {
    public static void main(String[] args){
        /*no design*/
        Api api = new Impl();
        api.sayHello("Zhang San");

        /*use design*/
        Api api2 = HelloSimpleFactory.getInstance();
        api2.sayHello("Li Si");


    }
}
