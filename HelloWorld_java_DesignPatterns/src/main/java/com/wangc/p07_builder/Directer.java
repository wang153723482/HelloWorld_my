package com.wangc.p07_builder;

/**
 * @author: wangchao
 * Date: 2016/3/21 9:18
 * Description: 按照一定的步骤，依次调用获取组件
 */
public class Directer {
    Builder builder;

    public Directer(Builder builder) {
        this.builder = builder;
    }

    public void constuct(){
        builder.builderA();
        builder.builderB();
    }
    
}
