package com.wangc.fast.p3

import scala.collection.mutable.ArrayBuffer
import scala.util.Random

/**
  * Created by wangchao on 2017/6/7.
  */
object Study3_test {
  def main(args: Array[String]): Unit = {
    println("1===================")
    val n = 5
    val r = new Random()
    r.nextInt(n)
    val result = for(i<-0 until n)yield r.nextInt(n)
    println(result)

    println("2===================")
    //写一个循环，将整数数组中相邻的元素置换。例如Array(1,2,3,4,5)变成 Array(2,1,4,3,5)
    val a2 = Array(1,2,3,4,5)
    for( i <- 0 until a2.length by 2 ){
      val tmp = a2(i)
      if( i+1 < a2.length ){ 
        a2(i) = a2(i+1)
        a2(i+1) = tmp
      }
    }
    println( a2.mkString )

    println("3===================")
    //重复上一个 ，生成新的数组，使用for/yield
    

    println("4===================")
    //把数组排序，所有正数按原顺序，然后是所有的0或负数按原顺序
    val a4 = Array(3,5,-6,-9,0,1)
    var s4 = ArrayBuffer[Int]()
    for(i<-a4 if (i>0) ){ s4 += i }
    for(i<-a4 if (i<=0) ){ s4 += i }
    println( s4.toString() )


    println("5===================")
    val a5 = Array[Double](3.4,43.2)
    println( a5.sum )


    println("6===================")
    // Array[Int] 中的元素反序排列    ArrayBuffer[Int] 反序排列
    var a6 = Array(1,2,3)
    var b6 = ArrayBuffer(11,12,13)
    
    var a = 2
    var b= 4
    
    
    
    
  }

}
