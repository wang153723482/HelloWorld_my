package com.wangc.p06_abstract_factory;

/**
 * @author: wangchao
 * Date: 2016/3/7 9:47
 * Description:抽象的工厂，定义了工厂类能生产 ProductA 和 ProductB
 */
public interface AbstractFactory {
    
    public AbstractProductA createProductA();
    
    public AbstractProductB createProductB();
    
}
