package com.wangc.p22_decorator.test2;

/**
 * Created by wangchao on 2016/11/21.
 */
public class ChickenHamburg extends Hamburg {
    public ChickenHamburg() {
        name = "Chicken";
    }

    @Override
    public double getPrice() {
        return 12;
    }
}
