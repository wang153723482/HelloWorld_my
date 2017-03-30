package com.wangc.p22_decorator.test2;

/**
 * Created by wangchao on 2016/11/21.
 */
public class ComdimentB extends Comdiment {
    Hamburg h;

    public ComdimentB(Hamburg h) {
        this.h = h;
    }

    @Override
    public String getName() {
        return h.getName()+" i am b";
    }

    @Override
    public double getPrice() {
        return h.getPrice()+2;
    }
}
