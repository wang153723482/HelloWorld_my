package com.wangc.p06_abstract_factory;

/**
 * @author: wangchao
 * Date: 2016/3/7 9:51
 * Description:第一个工厂，只能生产 ProductA1 和 ProductB1 
 * （只能生产A产品的1型号和B产品的1型号，这两个产品只有都是1型号才能匹配）
 */
public class ConcreteFactory1 implements AbstractFactory {
    @Override
    public AbstractProductA createProductA() {
        return new ProductA1();
    }

    @Override
    public AbstractProductB createProductB() {
        return new ProductB1();
    }
}
