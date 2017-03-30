package com.wangc.p04_adapter.p04_2;

/**
 * @author: wangchao
 * Date: 2016/3/5 16:22
 * Description:
 */
public abstract class EventAdapter implements EventMy{

    @Override
    public void move() {
        System.out.println("you are moved by adapter");
    }

    @Override
    public void click() {
        
    }

    @Override
    public void doubleClick() {

    }

 
}
