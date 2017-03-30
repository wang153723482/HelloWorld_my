package com.wangc.function_interface;

import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;

/**
 * Created by wangchao on 2017/2/21.
 */
public class Test00Function {

    static void modifyTheValue(int i, Function<Integer,Integer> function){
        int newValue = function.apply(i);
        System.out.println(newValue);
    }
    
    public static void main(String[] args){
        
        int my = 23;
        int myss = 23;
        int m2y = 23;
        modifyTheValue(my,val->val+100);

        BinaryOperator a;
    }
}



