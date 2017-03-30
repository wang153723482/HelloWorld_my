package com.wangc.p01_simple_factory;

/**
 * @author: wangchao
 * Date: 2016/1/6 11:54
 * Description:
 */
public class HelloSimpleFactory {
    public static Api getInstance(){
        return new Impl();
    }
}
