package com.wangc;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import javax.websocket.server.PathParam;
import java.util.ArrayList;
import java.util.List;

import static javax.swing.text.html.FormSubmitEvent.MethodType.POST;

/**
 * Created by wangchao on 2017/2/9.
 */

@SpringBootApplication
//@RestController
@Controller
@RequestMapping("/test")
public class Ch72Application {
    
    @RequestMapping("/index")
    public String index(Model model){
        Person person = new Person("wangchao",27);
        
        List<Person> list = new ArrayList<Person>();
        Person p1  = new Person("zhangsan",12);
        Person p2  = new Person("lisi",25); 
        Person p3  = new Person("zhaoliu",37);
        list.add(p1);
        list.add(p2);
        list.add(p3);
        
        model.addAttribute("single",person);
        model.addAttribute("people",list);
        
        
        System.out.println("=================wangc");
        return "index";
//        return "sdfasdf";
    }

    
    /*重载方法，指定不同的method*/
    @RequestMapping(path = "login",method = RequestMethod.GET)
    public String login(){
        System.out.println("===================get");
        return "login";
    }
    
    @RequestMapping(path = "login",method = RequestMethod.POST)
    public String login(Model model,Login login){
        System.out.println("===================post");
        System.out.println(model);
        System.out.println(null==model);
        System.out.println(login);
        System.out.println(login.getUsername());
        System.out.println(null==login);
        
        return "login";
    }

    
    /*请求路径是 login/123 ,下面的语句中则打印123 
    * 请求路径是 login/123/456 ,报错404*/
    @RequestMapping(path = "login/{userId}",method = RequestMethod.GET)
    public String pathValue(@PathVariable String userId){
        System.out.println("========get========"+userId);
        return "login";
    }

    /*用正则过滤路径*/
    @RequestMapping(path = "login/{userId}/{productId:[a-z]}",method = RequestMethod.GET)
    public String pathValue(@PathVariable String userId,@PathVariable String productId){
        System.out.println("========get========"+userId);
        System.out.println("========get========"+productId);
        return "login";
    }


    public static void main(String[] args){
        SpringApplication.run(Ch72Application.class,args);
    }
    
}
