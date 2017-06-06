package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/4.
  * Chapter 2.8 默认参数和带名参数
  */
object Study2_8 {
  def main(args: Array[String]): Unit = {
    println( decorate("hello") )//只有一个参数，第二个和第三个会使用默认值
    println( decorate("hello","<",">") )//使用传递的参数
    println( decorate("hello",right=">>") )//指定参数名字，PS:带名和不带名混用时，不带名的在前
    println( decorate("test","<<") )//参数列表的个数不一定匹配，按顺序匹配
    
  }
  
  def decorate(str:String,left:String="{",right:String="}")={
    left + str + right
  }

}
