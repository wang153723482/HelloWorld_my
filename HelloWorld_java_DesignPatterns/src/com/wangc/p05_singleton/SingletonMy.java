package com.wangc.p05_singleton;

/**
 * @author: wangchao
 * Date: 2016/3/5 19:19
 * Description:
 */
public class SingletonMy {
    
    private static SingletonMy singletonMy = null;
    
    //懒汉模式，只有在用到的时候才去初始化实例
    public static SingletonMy getInstance(){
        if(null==singletonMy){
            singletonMy = new SingletonMy();
        }
        return singletonMy;
    }
    
}

/*
//饿汉模式，加载的时候即初始化示例
public class SingletonMy {
    private static SingletonMy singletonMy = new SingletonMy();
    public static SingletonMy getInstance(){
        return singletonMy;
    }
}
*/
