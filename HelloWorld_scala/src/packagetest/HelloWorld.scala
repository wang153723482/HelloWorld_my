package wangc.packagetest

/*scala 没有静态方法和静态字段
* 通过关键字 object 实现静态类
* */

// 语句末尾的 ; 可有可无，idea建议去掉

object HelloWorld{
  
  def main(args:Array[String]){
    println( args )
    println( args(0) )
    println("Hello World,Scala!  xx")
    
    /*数据类型*/
    //Byte //Short //Int //Long //Float //Double
    //Char //String
    //Boolean
    
    //Unit 表示无值，类似void，但这是一种类型，只有一个值  ()
    //Null 
    //Nothing 任何类型的子类型
    //Any 任何类的超类
    //AnyRef 所有引用类的基类
    
    
    /*声明变量*/
    //声明使用var或val关键字，变量名后面使用冒号，后面是数据类型，后面是等号
    //指明数据类型，且有初始值
    //var 声明变量， val 声明常量，常量不能修改
    val FIRST_NAME : String = "wang"
    var name : String = "zhangsan"
    var age : Int = 25
    var flag : Boolean = false
    var flag2 = true
    
    //指明数据类型，没有初始值  todo 为什么会报错？
//    var init :String
                          
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
