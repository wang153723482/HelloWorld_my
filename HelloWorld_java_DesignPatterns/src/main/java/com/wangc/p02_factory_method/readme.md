### 工厂方法
包含4个角色

* 抽象工厂 Operate
* 具体工厂 OperateExportDb OperateExportTxt
* 抽象产品 ExportFileApi
* 具体产品 ExportDbFile ExportTextFile

在抽象工厂中，创建了一个获取抽象产品的抽象方法，该方法返回的抽象产品调用自身定义的方法。
使用时，实例化某一个实现工厂，在实现工厂中，创建了具体的产品，即调用具体产品的自身方法。

2017-02-07
抽象工厂中的抽象方法，生成的是一个抽象的产品。
具体工厂实现该抽象方法，生成具体的产品。