package com.wangc.p02_factory_method;

/**
 * @author: wangchao
 * Date: 2016/1/7 21:12
 * Description:
 */
public class ExportTxtFile implements ExportFileApi {
    @Override
    public boolean export(String data) {
        System.out.println("导出了txt文件");
        return true;
    }
}
