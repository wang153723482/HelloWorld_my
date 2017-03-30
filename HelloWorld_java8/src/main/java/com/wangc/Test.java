package com.wangc;

import java.util.UUID;

/**
 * Created by wangchao on 2017/3/16.
 */
public class Test {
    public static void main(String[] args){
        System.out.println(UUID.randomUUID().toString().replace("-",""));
        System.out.println(UUID.randomUUID().toString().replace("-",""));
        System.out.println(UUID.randomUUID().toString().replace("-",""));
        System.out.println(UUID.randomUUID().toString().replace("-",""));

        String str ="{\"username\":\"JerryAndTom\",\"password\":\"123456\"" +
                ",\"email\":\"88888@qq.com\"}";
        
        System.out.println(str);
    }
}
