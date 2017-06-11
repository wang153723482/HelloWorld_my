package com.wangc.fast.p3

/**
  * Created by wangchao on 2017/6/7.
  * Chapter 3.1 长度不可变的数组
  */
object Study3_1 {
  def main(args: Array[String]): Unit = {
    //使用val声明
    
    val a = new Array[Int](10) //初始一个长度为10的数组，每个值都初始为0
//    a = new Array[Int](11) //重新个a赋值时，编译报错，但是并不影响修改数组中的值
    println(a(0))
    println(a(9))
    a(0) = 111
    a(9) = 112
    println(a(0))
    println(a(9))
    println("==============================")
    
    val s = new Array[String](10) //初始一个长度为10的数据，每个值都初始为 null
    println(s(0))
    println(s(9))
    println("==============================")
    
    val s2 = Array[String]("a","b","c") // 不用new，直接通过赋值的方式进行初始化
    //val s2 = Array("a","b","c")  //可以不指定类型，类型是推断出来 
    println(s2(0))
  }

}
