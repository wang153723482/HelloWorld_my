package com.wangc.fast.p6

/**
  * Created by wangchao on 2017/6/15.
  */
object AccountsTest {

  def main(args:Array[String]): Unit ={
    println( Accounts.newUniqueNumber() )
    println( Accounts.newUniqueNumber() )
    println( Accounts.newUniqueNumber() )
    
    var acc = Accounts //因为实现 了apply() 方法
    println( acc.newUniqueNumber() )
    
    val a1 = Array(1,2,3)
    val a2 = new Array[String](2)
    a2(0) = "sss"
    a2(1) = "xxx"
    
  }
}
