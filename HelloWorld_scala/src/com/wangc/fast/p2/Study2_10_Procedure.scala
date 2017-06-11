package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/7.
  * Chapter 2.10 过程
  * 对于不返回值的函数，称为过程
  */
object Study2_10_Procedure {
  
  def main(args:Array[String]):Unit={
    testPro("hello")
  }
  
  //Unit 可以省略，但是惯例还是写上
  def testPro(str:String):Unit={
    println("=========")
    println("|"+str+"|")
    println("=========")
  }

}
