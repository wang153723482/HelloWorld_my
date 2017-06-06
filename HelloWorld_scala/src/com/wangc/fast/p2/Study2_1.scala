package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/1.
  * chapter 2.1 Conditional Expressions 
  * if表达式也是有值的
  */
object Study2_1 {
  def main(args: Array[String]): Unit = {
    val x = -3
    val s = if (x>0) 1 else -1
    // if (x>0) s = 1 else s = -1 //这两行效果一样，但是这样写只能使用var声明了
    println(s)
    
    val s2 = if (x>0) "success" else -1
    println(s2)
    println(s2.getClass.getSimpleName)
    
    val s3 = if (x>0) 23   
    //val s3 = if (x>0) 23 else ()  
    println(s3)

  }
}
