package com.wangc.fast.p2

import scala.io.StdIn

/**
  * Created by wangchao on 2017/6/1.
  * Chapter 2.4 Input and Output
  * 
  */
object Study2_4 {
  def main(args:Array[String]):Unit={
    
    print(1)
    println(2)
    
    val name = readLine("Your name:")
    println(name)
    
    print("Your age:")
    val age = readInt()
    println(age)
    
    //readLine() readInt() 已经是不推荐的方法了
    
    val name2 = StdIn.readLine("Your name:")
    println(name2)

    print("Your age:")
    val age2 = StdIn.readInt()
    println(age2)

  }
}
