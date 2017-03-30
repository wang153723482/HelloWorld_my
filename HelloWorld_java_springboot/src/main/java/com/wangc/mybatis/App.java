package com.wangc.mybatis;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.transaction.annotation.EnableTransactionManagement;

/**
 * Created by wangchao on 2017/2/14.
 */

@SpringBootApplication
@EnableTransactionManagement
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
