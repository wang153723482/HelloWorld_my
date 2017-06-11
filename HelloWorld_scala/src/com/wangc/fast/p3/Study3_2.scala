package com.wangc.fast.p3

import scala.collection.mutable.ArrayBuffer

/**
  * Created by wangchao on 2017/6/7.
  * Chapter 3.2 可变长度的数组 数组缓冲
  */
object Study3_2 {
  def main(args: Array[String]): Unit = {
    
    val b = ArrayBuffer[Int]()
    b += 11        //追加单个元素
    b += (21,22,23) //追加多个元素
    b.append(31)
    
    b ++= Array(31) //追加另外一个数组对象
    val b2 = Array[Int](32)
    b ++= b2
    
    println(b.toString())
    
    b.toArray // ArrayBuffer 转换为 Array
    b2.toBuffer // Array 转换为 ArrayBuffer
    
    val b3 = Array(2,33,4)
    println(b3.mkString(",")) // 输出数组
    
    println( b ) //ArrayBuffer 可以直接toString输出
    println( b3 ) // Array 只能输出内存地址
    
    
    
  }

}
