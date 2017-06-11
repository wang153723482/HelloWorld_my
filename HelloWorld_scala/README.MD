# scala 
hello world


在 scala 中，分为class和object
其中在 object 中，所有的方法和属性都是静态 static 的
PS:scala 没有static关键字

scala.collection.mutable._ 可变的集合, `ArrayBuffer`, `StringBuilder`, `HashMap`, `HashSet`
scala.collection.immutable._ 不可变的集合  `Vector`, `List`, `Range`, `HashMap` ,`HashSet`

在 scala 中，默认使用的不可变Map，如要使用可变的Map，需要指定包名
`scala.collection.mutable.Map`


###伴生类
在 scala 中，一个object和一个class使用相同的名字，且在同一个包路径下，
则class为object的伴生类，object为class的伴生对象。


