package com.wangc.p03_facade;

/**
 * @author: wangchao
 * Date: 2016/3/4 11:05
 * Description:
 */
public class Main {
    public static void main(String[] args){
        
        /*不用外观模式的话，调用者需要知道每一个具体的实现类*/
        Model1 model1 = new Model1();
        Model2 model2 = new Model2();
        model1.m1();
        model2.m2();
        
        System.out.println("===============================");
        
        /*使用外观模式，调用者仅知道一个中间类即可，不需要关心更具体的实现*/
        FacadeMy facadeMy = new FacadeMy();
        facadeMy.m();
        
    }
}
