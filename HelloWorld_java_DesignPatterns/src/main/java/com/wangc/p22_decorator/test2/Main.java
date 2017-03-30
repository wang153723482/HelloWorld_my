package com.wangc.p22_decorator.test2;

/**
 * Created by wangchao on 2016/11/21.
 */
public class Main {
    public static void main(String[] args){
        ChickenHamburg ch = new ChickenHamburg();
        ComdimentA ca = new ComdimentA(ch);
        ComdimentB cb = new ComdimentB(ca);
        
        System.out.println(cb.getName());
        System.out.println(cb.getPrice());
    }
}
