package com.wangc.sync;

/*
* 方法中使用synchronized关键字，参数为一个类
* 当使用多个实例调用时，锁也会生效*/

public class MySync3 {
    public void test3(){
        synchronized (MySync3.class){
            System.out.println("开始。。。。");
            try { Thread.sleep(1000);
            } catch (InterruptedException e) { e.printStackTrace(); }
            System.out.println("结束。。。");
        }
    }
}

class MySync3Thread extends Thread{
    @Override
    public void run() {
        new MySync3().test3();
    }
    public static void main(String[] args){
        new MySync3Thread().start();
        new MySync3Thread().start();
        new MySync3Thread().start();
    }
}
