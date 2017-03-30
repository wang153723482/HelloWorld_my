package com.wangc.p22_decorator.test1;

/**
 * Created by wangchao on 2016/11/14.
 * 日常奖金 = 销售额*0.01
 */
public class DecoratorB extends Decorator {

    public DecoratorB(Component c) {
        super(c);
    }

    @Override
    public double calcPrize(String user) {
        System.out.println(user+"日常奖金"+DBdate.USER_DATA.get(user)*0.01);
        return super.calcPrize(user) + DBdate.USER_DATA.get(user)*0.01;
    }
}
