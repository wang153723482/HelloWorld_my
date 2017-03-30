package com.wangc.p22_decorator.test1;

/**
 * Created by wangchao on 2016/11/14.
 * 装饰者的使用方法：
 * 先创建被装饰者，作为参数传入装饰者的构造方法
 */
public class Main {
    public static void main(String[] args){
        ConcreteComponent cc = new ConcreteComponent(); 
        
        Decorator da = new DecoratorA(cc);
        Decorator db = new DecoratorB(da);
        
        System.out.println( db.calcPrize("zhangsan") );
        
        System.out.println( db.calcPrize("lisi") );
    }
}
