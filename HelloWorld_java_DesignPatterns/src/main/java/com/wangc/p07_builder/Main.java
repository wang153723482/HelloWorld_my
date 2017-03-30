package com.wangc.p07_builder;

/**
 * @author: wangchao
 * Date: 2016/3/21 9:22
 * Description:
 */
public class Main {
    public static void main(String[] args){
        
        Builder builder = new Builder();
        Directer directer = new Directer(builder);
        
        directer.constuct();
        builder.getResult();
        
    }
}
