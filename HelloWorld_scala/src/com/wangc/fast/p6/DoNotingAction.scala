package com.wangc.fast.p6

/**
  * Created by wangchao on 2017/6/15.
  */
class DoNotingAction extends UndoableAction("Do Noting"){
  
  override def undo(){
    println("i am undo")
  }

  override def redo() = {
    println("i am redo")
  }
}
