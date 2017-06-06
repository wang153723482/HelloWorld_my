package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/1.
  * Chapter 2.3 Block Expressions and Assignments
  *  
  */
object Study2_3 {
  def main(args:Array[String]):Unit={
    
    //块表达式的值，是块里的最后一个表达式的值。
    val s = {
      var a = 1
      var b = 2
      a+b
    }
    //val s = {var a = 1;var b = 2;a+b} //在一行中，用;分隔多个表达式
    println(s)
    
    //赋值表达式是没有值的，就是Unit
    val s2 = {var a = 1}
    println(s2)

    //赋值表达式是没有值的
    var x:Any = null 
    var y:Any = null
    x = y = 1   //在java中可以，scala中 x 是{y=1}的值
    println(x)
    println(y)
    
    
  }
}
