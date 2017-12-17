package com.wangc.sync;

/*
* 在方法声明上使用 sycchronized 关键字
* 只有使用同一个实例的时候，锁才会生效
* */

public class MySync {
    /*方法命名上使用 synchronized 关键字*/
    public synchronized void test(){
        System.out.println("开始。。。。");
        try { Thread.sleep(1000);
        } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.println("结束。。。");
    }
    
}

class MySyncThread extends Thread{

    @Override
    public void run() {
        new MySync().test();  /*运行时使用不同的实例去调用test().结果发现，锁并没有生效*/
    }

    public static void main(String[] args){
        System.out.println("MySyncThread");
        new MySyncThread().start();
        new MySyncThread().start();
        new MySyncThread().start();
    }
}

class MySyncThread2 extends Thread{
    MySync mySync;
    MySyncThread2(MySync mySync){
        this.mySync = mySync;
    }
    @Override
    public void run() {
        mySync.test();/*运行外部的实例去调用test(),结果发现，当同一个实例时，锁生效*/
    }
    public static void main(String[] args){
        System.out.println("MySyncThread2");
        MySync mySync = new MySync();
        new MySyncThread2(mySync).start();
        new MySyncThread2(mySync).start();
        MySync mySync2 = new MySync();
        new MySyncThread2(mySync2).start();
    }
}

