package com.wangc.p22_decorator.test1;

/**
 * Created by wangchao on 2016/11/14.
 * 装饰器的父类，要一个构造方法，参数是本模式中的超类(或超类的子类)，并可以执行该参数中的方法
 */
public class Decorator extends Component {

    Component c;
    public Decorator(Component c) {
        this.c = c;
    }

    public double calcPrize(String user){
        return c.calcPrize(user);
    }
}
