package com.wangc.p03_facade;

/**
 * @author: wangchao
 * Date: 2016/3/4 11:04
 * Description:
 */
public class FacadeMy {
    
    public void m(){
        Model1 model1 = new Model1();
        Model2 model2 = new Model2();
        
        model1.m1();
        model2.m2();
    }
    
}
