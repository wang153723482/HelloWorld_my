package com.wangc.fast.p5

import scala.beans.BeanProperty

/**
  * Created by wangchao on 2017/6/12.
  */
class Counter {
  private var value = 0

  def increment(){ value += 1 }
  def current(): Int = value

  
  var age1 = 100   //直接修改/获取该变量
  

  private var privateAge = 21


  
  private[this] var name = 0
  
  def testThis(counter: Counter): Unit ={
//    println( counter.name ) //private[this] 只能在自己的实例中调用
  }
  
  

  @BeanProperty var address:String = _
}
