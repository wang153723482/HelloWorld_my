package com.wangc.sync;

/*
* 在普通方法中使用synchronized关键字，参数为this
* 只有在使用同一个实例调用方法时，锁才会生效*/

public class MySync2 {
    public void test2(){
        synchronized (this){
            System.out.println("开始。。。。");
            try { Thread.sleep(1000);
            } catch (InterruptedException e) { e.printStackTrace(); }
            System.out.println("结束。。。");
        }

    }
}

class MySync2Thread extends Thread{
    @Override
    public void run() {
        new MySync2().test2();
    }

    public static void main(String[] args){
        new MySync2Thread().start();
        new MySync2Thread().start();
        new MySync2Thread().start();
    }
}

class MySync2Thread2 extends Thread{
    MySync2 mySync2;
    MySync2Thread2(MySync2 mySync2){
        this.mySync2 = mySync2;
    }
    @Override
    public void run() {
        mySync2.test2();
    }

    public static void main(String[] args){
        MySync2 mySync2 = new MySync2();
        new MySync2Thread2(mySync2).start();
        new MySync2Thread2(mySync2).start();
        new MySync2Thread2(mySync2).start();
    }                    
}
