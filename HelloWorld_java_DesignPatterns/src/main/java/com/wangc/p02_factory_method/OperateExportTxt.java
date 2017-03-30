package com.wangc.p02_factory_method;

/**
 * @author: wangchao
 * Date: 2016/1/7 21:17
 * Description:
 */
public class OperateExportTxt extends Operate {
    @Override
    protected ExportFileApi factoryMethod() {
        return new ExportTxtFile();
    }
}
