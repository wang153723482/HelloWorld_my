### 适配器模式
在main方法中，原本只能持有接口 Target 的实现类。
但现在要持有一个未实现Target的类Adaptee，并且此类不可修改或不方便修改（例如第三方类）
那就新建一个适配器类 Adapter，实现了Target接口，在对应的实现方法中，调用了Adaptee的方法。
这样，在main中，就可以持有Adapter实例并调用其中的方法，即可达到调用Adaptee中的方法。