package com.wangc.fast.p6

/**
  * Created by wangchao on 2017/6/15.
  */
abstract class UndoableAction(val desc :String) {
  def undo():Unit
  def redo():Unit
}
