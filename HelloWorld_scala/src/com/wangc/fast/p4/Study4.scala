package com.wangc.fast.p4


/**
  * Created by wangchao on 2017/6/8.
  * Chapter 4 映射 和 元组  Maps and Tuples
  */
object Study4 {
  def main(args: Array[String]): Unit = {

    var m1 = Map("zhang" -> 12, "li" -> 14)  //scala 中默认使用的不可变的Map
//    m1 = Map("zhang" -> 12) //使用var时，m1可变，但m1对应的对象是不可变的
    
    println(m1)
    
    
    
//    m1("xxx") = 11  //不可变，不能添加key
//    m1("zhang") = 13 //不可变，不能修改value
//    m1.remove("a") //不可变，不能移除元素
    println(m1)
    
    var m2 = scala.collection.mutable.Map("a"->1,"b"->2)
    println(m2)
    
    m2 = scala.collection.mutable.Map("a"->1,"b"->2)
    println(m2)
    m2("a") = 11
    m2("c") = 22
    m2 -= "a" //移除一个元素
    println(m2)
    
    var m3 = new scala.collection.mutable.HashMap[String,Int]     //初始一个空的map
    
    var a4 = "wang"->111
    println(a4)
    
    
    println( m1("zhang") )
//    println( m1("zhang1") )//如果map中没有zhang1 这个key，会抛出异常

    println( m1.get("zhang") )  //返回一个Some
    println( m1.get("zhangxxx") ) //返回None 
    
    println( m1.contains("zhang") ) //判断是否有这个key
    
    var re = m1.getOrElse("zhangxxx",0)      //推荐使用 getOrElse() 
    println(re)//如果key包含 zhangxxx ，则返回对应的值，否则返回0
    
    var a5 = scala.collection.mutable.Map("zhang"->11)
    a5("li") = 10
    
    for( (k,v)<-a5 ){
      println(k+"==="+v)
    }
    
    var ss = a5.keySet //获取所有的key
    println(ss)

    var aaa  = for( (k,v)<-a5 ) yield (v,k) // 交换key和value
    println( aaa )
    
    
    val sortmap = scala.collection.immutable.SortedMap("zhang"->21,"li"->12,"wang"->34)
    println(sortmap) //根据key排序
    
    val listMap = scala.collection.mutable.LinkedHashMap("zhang"->21,"li"->12,"wang"->34)
    
    
    
    //元组
    var t1 = (1,2,"xxx")
    println( t1._1 ) //元组从1开始，不是0
    
    
    
    var m21 = scala.collection.mutable.Map()
    
    
    var t11 = Tuple2("x","xx")
    println(t11._1)
    
  }
}
