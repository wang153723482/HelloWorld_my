package com.wangc.fast.p10

import com.wangc.fast.P8.{Person, Student}

/**
  * Created by wangchao on 2017/6/21.
  */
class LoggerMy2 extends Student with Logger{
  override def log(info: String): Unit = ???
}
