package com.wangc.p06_abstract_factory;

/**
 * @author: wangchao
 * Date: 2016/3/7 10:10
 * Description:
 */
public class Main {
    public static void main(String[] args){
        AbstractFactory af = new ConcreteFactory1();
        af.createProductA().calc();
        af.createProductB().sheep();
    }
}
