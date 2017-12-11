package com.wangc.generic;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*定义一个类，构造方法包含2个参数，这两个参数*/
/*
* http://www.runoob.com/java/java-generics.html
* https://www.ibm.com/developerworks/cn/java/j-lo-gj/index.html
* http://www.jianshu.com/p/8e761bb1a863
* 
* l类型安全，使用编译器做类型强制要求，比对程序员要求更容易控制风险
* 消除类型转换，减少出错和更加可读
* 性能，无需进行类型判断，通过泛型可执行得知对应的类型
* */
public class MyGenericClass<T,S> {
    private T t;
    private S s;
    
    MyGenericClass(T t,S s){
        this.t = t;
        this.s = s;
    }
    
    public void testMethod(){
        System.out.println(t.getClass()+"==="+s.getClass());
    }
    
    public static void main(String[] args){
        String s = "hello";
        int a = 123;
        MyGenericClass<String,Integer> m = new MyGenericClass<String, Integer>(s,a);
        m.testMethod();
        
        List list = new ArrayList();
        Map map = new HashMap();
        MyGenericClass<List,Map> m2 = new MyGenericClass<List,Map>(list,map);
        m2.testMethod();
    }
    
    
    
}
