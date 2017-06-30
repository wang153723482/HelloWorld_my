package com.wangc.fast.P8

/**
  * Created by wangchao on 2017/6/18.
  */
abstract class Person {
  var name:String = ""
  var age = 0
  
  def toStringMy(): String ={
    "name:"+name+",age:"+age
  }

  val name2: String //抽象字段，即没有初值的字段
  
  def id:Int //抽象方法，子类重写抽象方法时，不需要使用 override
  
  
  

}
