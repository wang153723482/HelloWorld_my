package com.wangc.p06_abstract_factory;

/**
 * @author: wangchao
 * Date: 2016/3/7 9:57
 * Description:
 */
public class ProductA1 implements  AbstractProductA {
    @Override
    public void calc() {
        System.out.println("this is ProductA1,i love ProductB1.");
    }
}
