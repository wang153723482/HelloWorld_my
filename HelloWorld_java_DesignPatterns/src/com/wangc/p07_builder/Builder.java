package com.wangc.p07_builder;

/**
 * @author: wangchao
 * Date: 2016/3/21 9:17
 * Description: 生成组件、产品
 */
public class Builder {
    public Part builderA(){
        System.out.println("build A");
        return null;
    }
    public Part builderB(){
        System.out.println("build B");
        return null;
    }
    
    public Product getResult(){
        System.out.println("get the Product");
        return null;
    }
}
