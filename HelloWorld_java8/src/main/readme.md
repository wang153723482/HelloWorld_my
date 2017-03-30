### 函数式接口中的方法

* 默认方法
* 静态方法
* 抽象方法(有且仅有一个)


### 常用的函数接口
* Function  
接收一个参数并产生一个结果
* Consumer  
接收一个参数不产生结果
* Predicate  
返回boolean //todo
* Supplier    
每次调用的时候返回一个不同的结果
* UnaryOperator  
继承Function
    >Represents an operation on a single operand that produces a result of the same type as its operand. This is a specialization of Function for the case where the operand and result are of the same type.  
    This is a functional interface whose functional method is Function.apply(Object).
 
* BinaryOperator  
继承BiFunction
    >Represents an operation upon two operands of the same type, producing a result of the same type as the operands. This is a specialization of BiFunction for the case where the operands and the result are all of the same type.  
    This is a functional interface whose functional method is BiFunction.apply(Object, Object).



* BinaryOperator<T> (T, T) T 求两个数的乘积（ *）




