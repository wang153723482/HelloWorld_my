package com.wangc.fast.p9

/**
  * Created by wangchao on 2017/6/20.
  */
object Study9_2_FileRead {
  def main(args: Array[String]): Unit = {
    val sou = scala.io.Source.fromFile("D:\\work\\HelloWorld_my\\HelloWorld_scala\\src\\com\\wangc\\fast\\p9\\t.txt","UTF-8")
    for (i<-sou.getLines()){
      println(i)
    }
    
    println("======================")
    println( sou.mkString ) 
  }

}
