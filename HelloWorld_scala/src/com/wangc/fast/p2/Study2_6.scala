package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/1.
  * Chapter 2.6 Advanced for Loops and for Comprehensions
  */
object Study2_6 {
  def main(args: Array[String]): Unit = {
    
    for( i<- 1 to 3;j<- 1 to 3){
      println(i+"----"+j)
    } 
    
    println("=====================")
    
    for(i<-1 to 3;j<-1 to 3 if i!=j){
      println(i+"----"+j)
    } 
    println("=====================")
    
    //在REPL中可以运行
//    for(i<-1 to 10){
//      yield i % 3
//    } 
    
  }

}
