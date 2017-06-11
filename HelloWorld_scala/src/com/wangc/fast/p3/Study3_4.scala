package com.wangc.fast.p3

/**
  * Created by wangchao on 2017/6/7.
  */
object Study3_4 {
  def main(args: Array[String]): Unit = {
    var a = Array(1,2,3,4,5,6,7,8,9)
    var result = for(i<-a if i%2==0)yield 2*i
    for (i<-result) print(i)
    
    println("=========")
    //函数式写法
    
    var aa = a.filter(_%2==0).map(_*3)
    for (i<-aa) print(i)
    println("======")
  }
}
