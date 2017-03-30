package com.wangc.mybatis.mapper;

import com.ibigsea.bootdao.entity.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

/**
 * Created by wangchao on 2017/2/14.
 */
@Mapper
public interface UserMapper {

    int sa(User user);



} 

