package com.wangc.p22_decorator.test1;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by wangchao on 2016/11/14.
 */
public class DBdate {
    
    public static Map<String,Double> USER_DATA = new HashMap<String,Double>();
    
    static {
        USER_DATA.put("zhangsan",20000.0);
        USER_DATA.put("lisi",10000.0);
        USER_DATA.put("wangwu",30000.0);
    }
}
