package com.wangc.fast.p5

/**
  * Created by wangchao on 2017/6/12.
  */
object Study5_1 {
  
  def main(args:Array[String]):Unit={
    val cou = new Counter
    cou.increment()
    println( cou.current() )
    
    cou.age1_=(11)//等同 cou.age = 11 默认会有一个 xx_=() 的set方法
    println( cou.age1 )//将调用 cou.age1() 这个方法
    
    
    var p = new Person
    p.name = "zhangsan" //等同 p.name_=("zhangsan")
    println( p.name )
    
    p.setName("wangwu")
    println( p.getName )
    
    
    var ps = new PersionSuper("wangc",12)
    println( ps.name )
    println(ps.age)
    
    
    
  }

}
