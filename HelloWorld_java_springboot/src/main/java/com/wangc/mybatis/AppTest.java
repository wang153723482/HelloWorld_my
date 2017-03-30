package com.wangc.mybatis;

/**
 * Created by wangchao on 2017/2/14.
 */
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import com.ibigsea.bootdao.entity.User;
import com.ibigsea.bootdao.mapper.UserMapper;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = {App.class})
//相当于  --spring.profiles.active=dev  
@ActiveProfiles(value="dev")
public class AppTest {

    @Autowired
    private UserMapper mapper;

    @Test
    public void testInsert(){
        User user = new User();
        user.setUserName("张三");
        user.setAge(23);
        mapper.sa(user);
        System.out.println("插入用户信息"+user.getUserName());
    }

}  