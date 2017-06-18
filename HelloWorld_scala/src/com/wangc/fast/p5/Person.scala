package com.wangc.fast.p5

import scala.beans.BeanProperty


/**
  * Created by wangchao on 2017/6/13.
  */
class Person {

  //使用该注解，生成4个方法
  // name:String
  // name_(newValue:String):Unit
  // getName():String
  // setName(newValue:String):Unit
  @BeanProperty var name:String = _
  @BeanProperty var age:Int = _

  
  // 第一个辅助构造器
  def this(name:String){
    this() //调用主构造器  ，没有显式定义主构造器，则拥有默认的无参主构造器
    this.name = name
  }

  // 第二个辅助构造器
  def this(name:String,age:Int){
    this()
    this.name = name
    this.age = age
  }
  
}
