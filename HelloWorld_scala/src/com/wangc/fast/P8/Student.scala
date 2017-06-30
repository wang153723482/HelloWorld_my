package com.wangc.fast.P8

/**
  * Created by wangchao on 2017/6/18.
  */
class Student extends Person{
  override def toStringMy(): String ={
    "this is override ==="+super.toStringMy()
  }
  
  override val name2 = "sd"

  override def id:Int = 12 
}


object Test{
  def main(args: Array[String]): Unit = {
    val stu:Person = new Student
    println( stu.getClass )
    println( stu.toStringMy() )
  }
}