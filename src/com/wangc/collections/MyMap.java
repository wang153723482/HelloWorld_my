package com.wangc.collections;
// https://zhuanlan.zhihu.com/p/28525770   
// http://blog.csdn.net/maoyeqiu/article/details/49363661  
// http://www.aizhuanji.com/a/Lx31EQ8V.html

import java.util.HashMap;
import java.util.Map;

/*
* 简化Map，假定所有的key都是String，所有的value都是int
* */
public class MyMap {
    
    private Node[] nodes;
    private int size;
    
    public void put(String key,String value){
        if( null == nodes ){
            nodes = new Node[5];//默认初始10个长度 todo 长度需要扩展
        }
        int index = indexOfKey(key);
        if( -1!=index ){
            nodes[index].value = value; 
        }else{
            nodes[size] = new Node(key,value);
            size++;
        }
    }
    
    public String get(String key){
        int index = indexOfKey(key); 
        if( -1!= index){
            return nodes[index].value;
        }
        return null; //没有这个key，返回null
    }
    
    public int size(){
        return this.size;
    }
    
    public void remove(String key){
        int index = indexOfKey(key);
        if(-1!=index){
            // TODO: wangc@2017/12/17   
        }
    }
    
    //判断nodes中是否存在当前需要的key,如果没有则返回-1
    private int indexOfKey(String key){
        for(int i=0; i<size; i++){
            if( key.equals( nodes[i].key ) ){
                return i; 
            }
        }
        return -1;
    }
    
    private static class Node{
        String key;
        String value;
        Node(String key,String value){
            this.key = key;
            this.value = value;
        }
    }
    
    public static void main(String[] args){
        MyMap myMap = new MyMap();
        myMap.put("name","wangc");
        System.out.println( myMap.size );
        myMap.put("age","18");
        myMap.put("city","beijing");
        myMap.put("city1","beijing");
        myMap.put("city2","beijing");
        System.out.println( myMap.size );
        myMap.put("city3","beijing");
        myMap.put("city4","beijing");
        myMap.put("city5","beijing");
        myMap.put("city6","beijing");
        myMap.put("city7","beijing");
        myMap.put("city8","beijing");
        myMap.put("city9","beijing");
        System.out.println( myMap.size );
        System.out.println( myMap.get("name") );
    }
    
}

