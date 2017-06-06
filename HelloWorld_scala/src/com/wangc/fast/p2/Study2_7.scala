package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/3.
  * Chapter 2.7 函数
  */
object Study2_7 {
  
  def main(args:Array[String]):Unit = {
    // scala 中 函数 与 方法 是两个东西。
    // 方法对对象进行操作，而函数不是
    // 也可以使用return ，但是建议不要使用
    
    println( calc(5) )
    println( sumDg(5) )
    
  }
  
  // 必须指定参数的类型，但是可以不指定返回值的类型
  // 如果是递归函数，必须指定返回值的类型
  def calc(n:Int)={
    var r = 10
    r = r+n
    r  // 会返回最后一个语句的值
//    r  = 111 // 如果最后一个语句是赋值，返回的是 ()
  }
  
  // 递归函数，必须指定返回值的类型
  def sumDg(n:Int):Int={
    if(n==0) 0 else if(n==1) 1 else (sumDg(n-2) + sumDg(n-1))
  }

}
