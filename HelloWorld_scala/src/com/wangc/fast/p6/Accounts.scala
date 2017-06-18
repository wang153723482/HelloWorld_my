package com.wangc.fast.p6

/**
  * Created by wangchao on 2017/6/15.
  */
object Accounts {
  
  
  private var lastNumber = 0 
  def newUniqueNumber(): Int ={
    lastNumber += 1
    lastNumber
  }
}


class Accounts{
  println("init")
  val id = Accounts.newUniqueNumber()
  private var balance = 0.0
  def deposit(amount:Double):Unit={
    balance += amount
  }

  def apply: Accounts = new Accounts()
  
}