package com.wangc.fast.p10

/**
  * Created by wangchao on 2017/6/21.
  */
class LoggerMy extends Logger{
  override def log(info: String): Unit = {
    println(info)
  }

  override def toString: String = {
    return "xxx"
  }
}
