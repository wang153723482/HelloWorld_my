package com.wangc.p02_factory_method;

/**
 * @author: wangchao
 * Date: 2016/1/7 21:13
 * Description:
 */
public class ExportDbFile implements ExportFileApi {
    @Override
    public boolean export(String data) {
        System.out.println("导出了db文件");
        return true;
    }
}
