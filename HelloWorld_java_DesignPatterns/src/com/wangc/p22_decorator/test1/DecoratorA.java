package com.wangc.p22_decorator.test1;

/**
 * Created by wangchao on 2016/11/14.
 * 业务奖金，销售额*3%
 */
public class DecoratorA extends Decorator {
    
    public DecoratorA(Component c) {
        super(c);
    }

    @Override
    public double calcPrize(String user) {
        System.out.println(user+"业务奖金"+DBdate.USER_DATA.get(user)*0.03);
        return super.calcPrize(user)+DBdate.USER_DATA.get(user)*0.03;
    }
}
