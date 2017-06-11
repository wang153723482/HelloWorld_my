package com.wangc.fast.p3

import java.util

import scala.collection.mutable.ArrayBuffer

/**
  * Created by wangchao on 2017/6/7.
  * Chapter 3.5 数组的常用算法
  */
object Study3_6 {
  def main(args: Array[String]): Unit = {
    val a = Array(1,2,3,4,5,99,10)
    println( a.sum )
    println( a.min )
    println( a.max )
    val b = a.sorted //min max sorted ，数组中的元素必须支持比较操作，包括数字、字符串、带有Ordered特质的类型（估计是继承或实现某一接口的类）
    for(i<-b){print(i+",")}
    
    var c = ArrayBuffer(5,33,2)
    c.append(13)
    println( c.count(_>10) )
    
    
  }

}
