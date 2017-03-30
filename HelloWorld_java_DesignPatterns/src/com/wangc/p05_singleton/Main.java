package com.wangc.p05_singleton;

/**
 * @author: wangchao
 * Date: 2016/3/5 19:19
 * Description:
 */
public class Main {
    public static void main(String[] args){
        
        SingletonMy s1 = SingletonMy.getInstance();
        SingletonMy s2 = SingletonMy.getInstance();
        SingletonMy s3 = SingletonMy.getInstance();
        
        System.out.println("s1="+s1);
        System.out.println("s2="+s2);
        System.out.println("s3="+s3);
        
    }
}
