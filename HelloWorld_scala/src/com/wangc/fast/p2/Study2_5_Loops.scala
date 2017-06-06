package com.wangc.fast.p2

/**
  * Created by wangchao on 2017/6/1.
  * Chapter 2.5 Loops
  */
object Study2_5_Loops {
  def main(args: Array[String]): Unit = {
    
    var n = 1
    var r = 0
    while (n > 0){
      println(n+"=="+r)
      r = r + n
      if (r>5){
        n = -1
      }
    }
    
    //[0,5] 前闭后闭
    for(i <- 0 to 5){
      println(i)
    }
    
    //[0,3) 前闭后开
    for(i <- 0 until 3){
      println(i)
    }
    
    println( 12 to 15 )
    
    for (ch <- "Hello"){
      println(ch)
    }
    
    //scala 中没有 break 和 continue ，使用一个flag来控制
    
    
    println("===============")
    test()
  }
  
  def test():Unit={
    //前闭后闭 [1,5]
    for (i <- 1 to 5){
      println(i)
    }
    //前闭后开 [1,5)
    for (i <- 1 until 20 if i%5==0){
      println(i)
    }
  }
  
}











