package com.wangc.p04_adapter.test1;

/**
 * Created by wangchao on 2017/3/1.
 */
public class ExportAdapter implements Export {
    @Override
    public void exc() {
        ExportNew exportNew = new ExportNew();
        exportNew.excNew();
    }
}
