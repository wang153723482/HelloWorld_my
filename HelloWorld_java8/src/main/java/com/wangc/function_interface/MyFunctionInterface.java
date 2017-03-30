package com.wangc.function_interface;

/**
 * Created by wangchao on 2017/2/21.
 */
@FunctionalInterface
public interface MyFunctionInterface {
    
    /*接口方法*/
    void te();
    
    /*默认方法*/
    default void sort(){
        
    }
    
    
    /*静态方法*/
    static void stMethod(){
        
    }
    
    
    
}
