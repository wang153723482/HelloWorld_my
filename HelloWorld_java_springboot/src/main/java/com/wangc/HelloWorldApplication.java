package com.wangc;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by wangchao on 2017/2/7.
 */

@SpringBootApplication
@RestController
public class HelloWorldApplication {
    
    @RequestMapping("/")
    String index(){
        return "Hello World Spring Boot.";
    }
    
    @RequestMapping("/new_path")
    String hello(){
        return "This is /new_path";
    }
    
    @RequestMapping("/two_path")
    String two(){
        return "This is /two_path";
    }
    
    public static void main(String[] args){
        SpringApplication.run(HelloWorldApplication.class,args);
    }
    
}
