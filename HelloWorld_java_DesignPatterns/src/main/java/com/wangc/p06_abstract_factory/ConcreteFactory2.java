package com.wangc.p06_abstract_factory;

/**
 * @author: wangchao
 * Date: 2016/3/7 9:54
 * Description: 只能生产 ProductA2 和 ProductB2 
 * 
 */
public class ConcreteFactory2 implements AbstractFactory {
    @Override
    public AbstractProductA createProductA() {
        return new ProductA2();
    }

    @Override
    public AbstractProductB createProductB() {
        return new ProductB2();
    }
}
