package com.wangc.p22_decorator.test3;

/**
 * Created by wangchao on 2016/12/27.
 */
public class ZhuangshiqiA extends Zhuangshiqi {
    public ZhuangshiqiA(Chengfen cf) {
        super(cf);
    }
    public void say(){
        System.out.println("i am a");
    }
}
