package com.wangc.fast.p9

/**
  * Created by wangchao on 2017/6/20.
  */
object Study9_10_Reg {
  def main(args: Array[String]): Unit = {
    val p = """[0-9]""".r
//    val p2 = "\s"  //因为这种情况，所以推荐使用三个双引号
    
    val target = "23kdf3hj6"
    
    for (matchStr <- p.findAllIn(target)){
      println( matchStr )
    }
  }

}
