package com.wangc.fast.p2

import scala.collection.immutable.StringOps

/**
  * Created by wangchao on 2017/6/6.
  */
object Study2_test {

  def main(args: Array[String]): Unit = {
     println( test1(1) )
    test2()
    test4()
    test6("Hello")

    var so = new StringOps("asdfghjkl")
    println(so*3)
    println( so.canEqual(so) )
    println( so.canEqual("a") )
    println( so.canEqual("asdfghjkl") )
  }
  
  def test1(x:Int): Int ={
    if(x>0){
      1
    }else if(x<0){
      -1
    }else{
      0
    } 
  }
  
  def test2(): Unit ={
    var a = {}
    println(a)  //值是 ()  ,类型是Unit
  }
  
  def test4(): Unit ={
    // for(int i=10;i>=0;i--)System.out.println(i);
    
//    for(i<- 10.to(1).by(-1) ){  //正常的写法，下面一行是简写
    for(i<- 10 to 1 by -1 ){
      println(i)
    }
  }
  
  def test5(n:Int): Unit ={
    for( i<- n to 0 by -1 ){
      println(i)
    } 
  }
  
  def test6(n:String): Unit ={
    var total:Int = 1
    for(i<-n){
      total = total*i
    }
    println(total)
  }
  
  
}











