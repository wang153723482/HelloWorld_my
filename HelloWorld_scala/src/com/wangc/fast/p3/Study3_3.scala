package com.wangc.fast.p3

/**
  * Created by wangchao on 2017/6/7.
  */
object Study3_3 {
  def main(args: Array[String]): Unit = {
    val a = Array[String]("aa","bb","cc","dd")
    for(i<- 0 until 3){//遍历每一个元素
      println( a(i) )
    }
    println("----------")
    for(i<- 0 until 3 by 2){//每隔一个遍历一次
      println( a(i) )
    }
    println("--------------------")
    for(i<- 0 until (3,2)){//每隔一个遍历一次
      println( a(i) )
    }
    println("------------------------------")
    for (i<-a){
      println(i)
    }

  }

}
