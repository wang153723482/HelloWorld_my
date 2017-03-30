package com.wangc.p02_factory_method;

/**
 * @author: wangchao
 * Date: 2016/1/7 21:18
 * Description:
 */
public class OperateExportDb extends Operate {
    @Override
    protected ExportFileApi factoryMethod() {
        return new ExportDbFile();
    }
}
