package com.wangc.p02_factory_method;

/**
 * @author: wangchao
 * Date: 2016/1/7 21:14
 * Description:
 */
public abstract class Operate {

    public boolean export(String data){
        ExportFileApi api = factoryMethod();
        return api.export(data);
    }

    protected abstract ExportFileApi factoryMethod();

}
