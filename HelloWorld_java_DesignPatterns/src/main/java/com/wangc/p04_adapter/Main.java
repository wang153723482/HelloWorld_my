package com.wangc.p04_adapter;

/**
 * @author: wangchao
 * Date: 2016/3/5 16:02
 * Description:
 */
public class Main {
    public static void main(String[] args){
        Target t;
        
        t = new Adapter();
        t.say();
    }
}
