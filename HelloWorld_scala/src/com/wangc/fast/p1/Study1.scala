package com.wangc.fast.p1

/**
  * Created by wangchao on 2017/6/1.
  * Chapter 1 
  * 在scala中的类型，参考图片 hier2.jpg
  * 图片出处：http://hongjiang.info/scala-null-and-nothing/
  * Any 类为所有类的超类
  * AnyVal Any类的子类，所有基本数据类型的父类 
  * AnyRef Any类的子类，所有引用类型的父类
  * 
  */
object Study1 {
  
  def main(args:Array[String]):Unit={
    /*基本数据类型*/
    //Byte //Short //Int //Long //Float //Double
    //Char 
    //Boolean

    //Unit 表示无值，类似void，但这是一种类型，只有一个值  () //todo 乌鸦觉得更像是java种的Null
    //Null 
    //Nothing 任何类型的子类型
    //Any 任何类的超类
    //AnyRef 所有引用类的基类


    /*声明变量*/
    //声明使用var或val关键字，变量名后面使用冒号，后面是数据类型，后面是等号
    //指明数据类型，且有初始值
    //var 声明变量， val 声明常量，常量不能修改
    //尽量使用val声明
    val FIRST_NAME : String = "wang"
    var name : String = "zhangsan"
    var age : Int = 25
    var flag : Boolean = false
    var flag2 = true

    //指明数据类型，没有初始值，在抽象类中可以  todo 为什么会报错？
//        var init :String

    //不一定指明数据类型，通过初始值推断出来的
    var hello = "i say hello"
    val count = 12
    //    var err //没有指明类型，且没有初始值，编译报错

    //使用val声明元组，元组不可变
    val myTuple = ("zhangsan","lisi")

    //数组

    var z:Array[String] = new Array[String](3)
    var z2 = new Array[String](3) //声明部分可以不指定类型

    z(0) = "zhangsan"
    z(1) = "lisi"
    println(z(1))

    var z3 = Array("nice","to","meet","you")
    var z4:Array[String] = Array("nice","to","meet","you")
    println(z3(0))
    println(z3.length)
    //    z3(4)="!"    //会报错，数组下标越界

    //数组不声明类型，则可以放入任意类型的值
    var intArr = Array(12,343,45,"sdf",34.34,'x')
    println( intArr.length )
    println(intArr(0))
    intArr(0)="aaaa"
    println(intArr(0)) //可以改变同一个位置的值的类型

    /*修饰符*/
    //public protected private

    
    /*方法调用*/
    // a.methodName(b)
    // 可以简写为  a methodName b
    

    /*运算符*/
    //跟java一样


    /*对象*/

    //    http://www.runoob.com/scala/scala-if-else.html

    sayHello("zhangsan")
    println( sayHello2("lisi") )
  }

  /*方法*/
  def sayHello(name:String): Unit ={
    //    name = "gougou " //方法形参为 val ，不可更改
    println("Hello" + name)
  }
  def sayHello2(name:String): String ={
    return "Hello "+name
  }


}
