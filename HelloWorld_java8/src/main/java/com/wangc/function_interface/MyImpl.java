package com.wangc.function_interface;

/**
 * Created by wangchao on 2017/2/21.
 */
public class MyImpl {
    
    public void test(MyFunctionInterface m){
        System.out.println(111);
        m.te();
    }
    
    public static void main(String[] args){
        
        MyImpl m = new MyImpl();
        m.test(()->System.out.print(11));
        
    }
}
