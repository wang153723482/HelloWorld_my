package com.wangc.p02_factory_method;

/**
 * @author: wangchao
 * Date: 2016/1/7 21:19
 * Description:
 */
public class Main {
    public static void main(String[] args){

        Operate operate = new OperateExportTxt();

        operate.export("abcdefghijkl");

    }
}
